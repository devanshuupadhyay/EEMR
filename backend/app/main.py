# backend/app/main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from tinydb import TinyDB
import structlog
import time
import os
from ._observability import init_sentry 
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

db = TinyDB(os.path.join(DATA_DIR, "db.json"))
users_table = db.table("users")
audit_table = db.table("audit")

logger = structlog.get_logger()

app = FastAPI(title="Easy EMR")

# Initialize observability
init_sentry(app) 

class UserIn(BaseModel):
    username: str
    display_name: str | None = None

@app.middleware("http")
async def audit_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    audit_table.insert({
        "path": str(request.url.path),
        "method": request.method,
        "status_code": response.status_code,
        "duration": duration
    })
    logger.info("request", path=str(request.url.path), method=request.method, status=response.status_code, duration=duration)
    return response

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/demo/create-user")
async def create_user(payload: UserIn):
    # Demo: one-click user creation for local demo only (DO NOT use in production)
    users_table.insert(payload.model_dump())
    return {"created": payload.username}
