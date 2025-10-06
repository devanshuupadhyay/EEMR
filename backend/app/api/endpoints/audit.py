# backend/app/api/endpoints/audit.py
from fastapi import APIRouter, HTTPException, Query
import structlog
from typing import Optional, List

from dbModels.db import audit_table
from ..models.audit import PaginatedAuditResponse, AuditLog

router = APIRouter()
logger = structlog.get_logger(__name__)

@router.get("/audit", response_model=PaginatedAuditResponse)
async def get_all_audit_logs(
    search_path: Optional[str] = None,
    search_method: Optional[str] = None,
    search_status: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(15, ge=1, le=100)
):
    """
    Get paginated and searchable audit logs from the database with per-column filtering.
    """
    try:
        logs = audit_table.all()

        # --- NEW: Per-column filtering logic ---
        if search_path:
            logs = [log for log in logs if search_path.lower() in log['path'].lower()]
        
        if search_method:
            logs = [log for log in logs if search_method.lower() in log['method'].lower()]

        if search_status:
            # Check if status code is a number before converting
            if search_status.isdigit():
                status_code_filter = int(search_status)
                logs = [log for log in logs if log['status_code'] == status_code_filter]
            else:
                # If search_status is not a number, return no results for this filter
                logs = []

        # Sort logs with the newest first
        sorted_logs = sorted(logs, key=lambda x: x.doc_id, reverse=True)
        
        total_logs = len(sorted_logs)
        
        # Calculate start and end for slicing
        start = (page - 1) * limit
        end = start + limit
        
        paginated_logs = sorted_logs[start:end]

        return {"total": total_logs, "logs": paginated_logs}

    except Exception as e:
        logger.exception("Error retrieving audit logs")
        raise HTTPException(status_code=500, detail="Internal Server Error")