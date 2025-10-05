# backend/app/api/models/fhir/patient.py
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.identifier import Identifier

__all__ = ["Patient", "HumanName", "Identifier"]