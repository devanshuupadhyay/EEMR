# backend/app/api/models/fhir/patient.py
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.identifier import Identifier
from fhir.resources.address import Address
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.attachment import Attachment
from fhir.resources.extension import Extension
from fhir.resources.reference import Reference

__all__ = ["Patient", "HumanName", "Identifier", "Address", "CodeableConcept", "ContactPoint", "Attachment", "Extension", "Reference"]