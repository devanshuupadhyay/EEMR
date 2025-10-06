# backend/app/main.py
from fastapi import FastAPI, Request, Depends, HTTPException
# --- ADD THIS IMPORT ---
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
import structlog
import time

# Import your project's modules
from .api.endpoints import patients
from ._observability import init_sentry, init_structlog, init_prometheus, init_tracing
from opentelemetry import trace
from auth.auth import create_access_token, verify_password, require_role
from dotenv import load_dotenv
from dbModels.db import audit_table, users_table
from .api.endpoints import patients, audit

load_dotenv()

app = FastAPI(title="Easy EMR")

# --- ADD THIS MIDDLEWARE SECTION ---
origins = [
    "http://localhost:3000", # The address of your frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)
# --- END NEW SECTION ---


app.include_router(patients.router, prefix="/api/v1", tags=["Patients"])
app.include_router(audit.router, prefix="/api/v1", tags=["Audit"])

# Initialize observability
init_structlog()
logger = structlog.get_logger()
#init_sentry(app)
init_prometheus(app)
#init_tracing(app)


@app.middleware("http")
async def observability_middleware(request: Request, call_next):
    """
    Middleware that logs request info (Structlog),
    records duration in TinyDB audit table,
    and automatically creates an OpenTelemetry span.
    """
    if request.url.path == "/metrics":
        return await call_next(request)
        
    start_time = time.time()
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span(f"{request.method} {request.url.path}"):
        response = await call_next(request)
        duration = time.time() - start_time

        audit_table.insert({
            "path": str(request.url.path),
            "method": request.method,
            "status_code": response.status_code,
            "duration": duration
        })

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

