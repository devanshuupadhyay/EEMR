from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    physician = "physician"
    staff = "staff"

class User(BaseModel):
    id: int
    username: str
    password_hash: str
    role: UserRole

class Patient(BaseModel):
    id: str
    first_name: str
    last_name: str
    dob: date
    gender: str
    insurance: Optional[str] = None

class Appointment(BaseModel):
    id: str
    patient_id: str
    physician_id: str
    date: date
    time: str
    notes: Optional[str] = None

class Encounter(BaseModel):
    id: str
    patient_id: str
    physician_id: str
    soap_notes: dict  # {"S": ..., "O": ..., "A": ..., "P": ...}

class Prescription(BaseModel):
    id: str
    patient_id: str
    physician_id: str
    medication: str
    dosage: str
    frequency: str

class LabOrder(BaseModel):
    id: str
    patient_id: str
    test_name: str
    status: str  # pending, completed

class LabResult(BaseModel):
    id: str
    order_id: str
    result: str
    file_path: Optional[str] = None

class BillingRecord(BaseModel):
    id: str
    patient_id: str
    encounter_id: str
    amount: float
    paid: bool = False
