# backend/app/main.py
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from tinydb import TinyDB, Query
from passlib.context import CryptContext
import structlog
import time
import os
import sys

from ._observability import init_sentry, init_structlog, init_prometheus, init_tracing
from opentelemetry import trace

from models.crud import add_user, get_user_by_username
from auth.auth import create_access_token, verify_password, require_role
from models.models import User, Appointment, Encounter, Prescription, LabOrder, LabResult, BillingRecord
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

db = TinyDB(os.path.join(DATA_DIR, "db.json"))
users_table = db.table("users")
audit_table = db.table("audit")

app = FastAPI(title="Easy EMR")

# Initialize observability
init_structlog() 
logger = structlog.get_logger()
init_sentry(app) 
init_prometheus(app)
init_tracing(app)

class UserIn(BaseModel):
    username: str
    display_name: str | None = None

@app.middleware("http")
async def observability_middleware(request: Request, call_next):
    """
    Middleware that logs request info (Structlog),
    records duration in TinyDB audit table,
    and automatically creates an OpenTelemetry span.
    """
    start_time = time.time()
    # Create a tracing span for this request
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span(f"{request.method} {request.url.path}"):
        response = await call_next(request)
        duration = time.time() - start_time

        # Record audit in TinyDB
        audit_table.insert({
            "path": str(request.url.path),
            "method": request.method,
            "status_code": response.status_code,
            "duration": duration
        })

        # Log structured message with Structlog
        logger.info(
            "http_request",
            path=str(request.url.path),
            method=request.method,
            status=response.status_code,
            duration=duration
        )

    return response

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/demo/create-user")
async def create_demo_users():
    from models import User
    demo_users = [
        User(username="admindemo", email="admindemo@test.com", hashed_password="", role="admin"),
        User(username="doc", email="doc@test.com", hashed_password="", role="physician"),
        User(username="staff", email="staff@test.com", hashed_password="", role="staff"),
    ]
    for u in demo_users:
        add_user(u)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/admin-only")
async def admin_endpoint(user: dict = Depends(require_role("admin"))):
    return {"message": f"Hello {user['username']}, you are an admin!"}

@app.post("/signup")
async def signup(user: "User"):
    from models import User
    existing = get_user_by_username(user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    add_user(user)
    return {"message": "User created successfully"}
