# backend/app/main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from tinydb import TinyDB, Query
from passlib.context import CryptContext
import structlog
import time
import os
from ._observability import init_sentry, init_structlog, init_prometheus, init_tracing
from opentelemetry import trace
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
async def create_user(payload: UserIn):
    # Demo: one-click user creation for local demo only (DO NOT use in production)
    users_table.insert(payload.model_dump())
    return {"created": payload.username}
