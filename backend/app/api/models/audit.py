# backend/app/api/models/audit.py
from pydantic import BaseModel
from typing import List, Optional

class AuditLog(BaseModel):
    path: str
    method: str
    status_code: int
    duration: float

class PaginatedAuditResponse(BaseModel):
    total: int
    logs: List[AuditLog]