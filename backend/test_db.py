from datetime import date
from models.models import User, Patient, Appointment
from models.crud import add_user, add_patient, add_appointment, get_user_by_id, get_patient_by_id, get_appointment_by_id

# Test user
u = User(id="u1", username="admin", role="admin")
add_user(u)
print(get_user_by_id("u1"))

# Test patient
p = Patient(id="p1", first_name="John", last_name="Doe", dob=date(1990,1,1), gender="M")
add_patient(p)
print(get_patient_by_id("p1"))

# Test appointment
a = Appointment(id="a1", patient_id="p1", physician_id="u1", date=date(2025,9,7), time="09:00")
add_appointment(a)
print(get_appointment_by_id("a1"))
