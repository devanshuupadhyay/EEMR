import os
from tinydb import TinyDB, Query

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize TinyDB
db = TinyDB(os.path.join(DATA_DIR, "db.json"), indent=4)

# Existing tables
users_table = db.table("users")
audit_table = db.table("audit")

# Milestone 2 tables
patients_table = db.table("patients")
appointments_table = db.table("appointments")
encounters_table = db.table("encounters")
prescriptions_table = db.table("prescriptions")
lab_orders_table = db.table("lab_orders")
lab_results_table = db.table("lab_results")
billing_table = db.table("billing")
