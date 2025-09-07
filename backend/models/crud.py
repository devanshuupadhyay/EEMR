from datetime import date
from tinydb import Query
from .db import (
    users_table,
    audit_table,
    patients_table,
    appointments_table,
    encounters_table,
    prescriptions_table,
    lab_orders_table,
    lab_results_table,
    billing_table
)
from .models import User, Patient, Appointment, Encounter, Prescription, LabOrder, LabResult, BillingRecord

# ---------- User CRUD ----------
def add_user(user: User):
    users_table.insert(user.model_dump())

def get_user_by_id(user_id: str):
    q = Query()
    return users_table.get(q.id == user_id)

# ---------- Patient CRUD ----------
def add_patient(patient: Patient):
    patient_dict = patient.model_dump()
    if isinstance(patient_dict.get("dob"), date):
        patient_dict["dob"] = patient_dict["dob"].isoformat()
    patients_table.insert(patient_dict)

def get_patient_by_id(patient_id: str):
    q = Query()
    result = patients_table.get(q.id == patient_id)
    if result and "dob" in result:
        result["dob"] = date.fromisoformat(result["dob"])
    return result

# ---------- Appointment CRUD ----------
def add_appointment(appointment: Appointment):
    appt_dict = appointment.model_dump()
    if isinstance(appt_dict.get("date"), date):
        appt_dict["date"] = appt_dict["date"].isoformat()
    appointments_table.insert(appt_dict)

def get_appointment_by_id(appointment_id: str):
    q = Query()
    result = appointments_table.get(q.id == appointment_id)
    if result and "date" in result:
        result["date"] = date.fromisoformat(result["date"])
    return result

# ---------- Encounter CRUD ----------
def add_encounter(encounter: Encounter):
    encounters_table.insert(encounter.model_dump())

def get_encounter_by_id(encounter_id: str):
    q = Query()
    return encounters_table.get(q.id == encounter_id)

# ---------- Prescription CRUD ----------
def add_prescription(prescription: Prescription):
    prescriptions_table.insert(prescription.model_dump())

def get_prescription_by_id(prescription_id: str):
    q = Query()
    return prescriptions_table.get(q.id == prescription_id)

# ---------- LabOrder CRUD ----------
def add_lab_order(order: LabOrder):
    lab_orders_table.insert(order.model_dump())

def get_lab_order_by_id(order_id: str):
    q = Query()
    return lab_orders_table.get(q.id == order_id)

# ---------- LabResult CRUD ----------
def add_lab_result(result: LabResult):
    lab_results_table.insert(result.model_dump())

def get_lab_result_by_id(result_id: str):
    q = Query()
    return lab_results_table.get(q.id == result_id)

# ---------- Billing CRUD ----------
def add_billing_record(record: BillingRecord):
    billing_table.insert(record.model_dump())

def get_billing_record_by_id(record_id: str):
    q = Query()
    return billing_table.get(q.id == record_id)

# ---------- Audit Logging ----------
def add_audit_log(entry: dict):
    audit_table.insert(entry)
