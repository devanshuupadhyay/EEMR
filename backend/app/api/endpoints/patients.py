# backend/app/api/endpoints/patients.py
from fastapi import APIRouter, HTTPException
from tinydb import Query
import structlog
import json
from typing import List # <--- Import List for type hinting

from models.db import patients_table
from ..models.fhir.patient import Patient

# Initialize router and logger
router = APIRouter()
logger = structlog.get_logger(__name__)

# --- NEW FUNCTION START ---
@router.get("/Patient", response_model=List[Patient])
async def get_all_patients():
    """
    Get all patients from the database.
    """
    try:
        all_patients_data = patients_table.all()
        # Convert each patient dict back into a Patient model
        return [Patient(**p) for p in all_patients_data]
    except Exception as e:
        logger.exception("Error retrieving all patients")
        raise HTTPException(status_code=500, detail="Internal Server Error")
# --- NEW FUNCTION END ---

@router.post("/Patient", response_model=Patient)
async def create_patient(patient: Patient):
    """
    Create a new patient.
    The request body must be a FHIR Patient resource.
    """
    try:
        patient_json_string = patient.model_dump_json()
        patient_data = json.loads(patient_json_string)
        patients_table.insert(patient_data)
        return patient
    except Exception as e:
        logger.exception("Error creating patient")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/Patient/{patient_id}", response_model=Patient)
async def get_patient(patient_id: str):
    """
    Get a patient by their ID.
    """
    try:
        PatientQuery = Query()
        patient_data = patients_table.get(PatientQuery.id == patient_id)
        if patient_data:
            return Patient(**patient_data)
        
        raise HTTPException(status_code=404, detail="Patient not found")
    except Exception as e:
        logger.exception("Error retrieving patient")
        raise HTTPException(status_code=500, detail="Internal Server Error")