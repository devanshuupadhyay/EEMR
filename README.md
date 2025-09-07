# Project Development Plan for EasyEMR

This document outlines the development plan for **EasyEMR**, a lightweight and efficient electronic medical records system.

## Milestone 1: Project Foundations 
### Step 1 Repo & Environment Setup
*   Create a GitHub repository and establish a robust branch strategy (`main` for production, `dev` for integration).
*   Configure Docker for both frontend and backend services to ensure consistent development and deployment environments.
*   Implement a GitHub Actions CI/CD pipeline for automated testing, linting, and deployment to a cloud service like Render.
*   Establish a basic FastAPI project structure, including URL path versioning (`/api/v1/...`).
### Dev steps
*   mkdir backend, frontend, .vscode
*   ni .gitignore -Force | Out-Null
#### create python venv and activate
*   python -m venv .venv
#### allow running the activation script in this session, then activate
*   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
. .\.venv\Scripts\Activate.ps1

#### make backend directory and install dependencies
*   mkdir backend\app -Force
*   cd backend
*   pip install --upgrade pip
*   create requirement.txt
*   fastapi "uvicorn[standard]" pydantic tinydb dramatiq[redis] redis structlog sentry-sdk python-dotenv
*   pip install -r requirements.txt

#### Create backend/app/main.py
Explanation:
*   TinyDB keeps everything file-based and easy to inspect (ideal for single-physician demo).
*   audit_middleware logs each HTTP request into an audit table — gives you an audit trail for Milestone 1.
*   create-user route satisfies the “one-click user creation for simple demo” requirement (but note the security warning).

### Step 2 — Background worker skeleton (Dramatiq) with Redis broker
*   Create backend/app/tasks.py
*   add a minimal background worker and Redis broker so you can queue background jobs (e.g., sending emails).

### Step 3 — Frontend: scaffold Nuxt 3 + Tailwind placeholder
*   create frontend/ using Nuxt 3, install Tailwind & Flowbite (Flowbite will be added later).
*   npx nuxi@latest init frontend
*   cd frontend
*   npm install --save-dev tailwindcss postcss autoprefixer
*   npm install flowbite pinia

#### Step 4 — Docker Compose skeleton (backend + redis + frontend)
* Create docker-compose.yml at project root

#### Step 5 — VS Code workspace ergonomics: Tasks + Debugging + Extensions
* add .vscode helpers so anyone opening the repo can start the stack with minimal typing.
    *   extensions.json (Recommended extensions)
    *   tasks.json (start backend/frontend quickly)
    *   Debugging launch.json for FastAPI (Python)   

#### Step 6 — Linting, formatting & CI skeleton
add black/flake8 for Python and ESLint/Prettier for frontend; add a basic GitHub Actions workflow to run checks on push.
*   Install Python tools (inside the venv):
*   cd .venv
*   pip install black isort flake8
*   Install frontend linters (inside frontend):
*   cd frontend
*   npm install -D eslint prettier
*   cd ..
*   mkdir -p .github\workflows

#### Step 7 — Observability & Logging starter
wire up structlog (done in the sample main.py) and provide a placeholder for Sentry/OpenTelemetry.
*   Add minimal Sentry + OpenTelemetry bootstrap in backend/app/_observability.py (load from env in main.py)


### Database & Models
*   Initialize TinyDB with JSON file storage to provide a simple, file-based database solution.
*   Define the following Pydantic models for data validation and consistency
*   Create a generic data access layer to abstract database operations.

#### 1. Database Setup

**Purpose:** Persist application data in a lightweight and accessible format.

* **Database:** TinyDB (JSON-based, file storage)
* **Data directory:** Created for storing `db.json`.
* Tables for each entity ensure organized separation of data.
* Allows for quick prototyping without complex database setup.

---

#### 2. Data Models

**Purpose:** Define structured data objects for all entities using Pydantic.

* **User:** Authentication and role information.

* **Patient:** Demographics and insurance information.

* **Appointment:** Scheduling, conflict checking, and physician association.

* **Encounter:** SOAP notes, visit records.

* **Prescription:** Medication details linked to encounters.

* **LabOrder / LabResult:** Orders and results of tests and imaging.

* **BillingRecord:** Financial records, CPT/ICD codes.

* Pydantic ensures **data validation and type safety**.

* Models define **fields, optional fields, and default values**.

---

#### 3. Tables and Access Layer

**Purpose:** Provide structured access to each table.

* Each entity gets its own TinyDB table (e.g., `users`, `patients`, `appointments`).
* A generic data access layer provides **CRUD operations**.
* Enables future expansion, e.g., migration to relational DB if needed.

#### 4. Observability Integration

* While not full observability, database actions are logged into **audit table**.
* Ensures traceability of data changes for compliance and debugging.

---

#### 5. How It Works Together

| Component         | Purpose                                      |
| ----------------- | -------------------------------------------- |
| TinyDB            | Lightweight JSON database for persistence    |
| Pydantic Models   | Structured, validated data for all entities  |
| Tables            | Separate storage per entity for organization |
| Data Access Layer | CRUD operations and abstraction over raw DB  |
| Audit Table       | Track data changes for observability         |

* This foundation allows later milestones (Patient Management, Appointments, Billing) to **operate on consistent, validated data**.

---

* EasyEMR’s database uses **TinyDB + Pydantic** for simplicity and structure.
* Clear separation of concerns: models define data, tables store it, access layer manipulates it.
* Audit logging ensures traceability even in a lightweight system.
* Provides a foundation for all future features and observability.


### Observability
*   Integrate Structlog for structured and contextual logging.
*   Set up Prometheus and Grafana for monitoring application metrics and visualizing performance dashboards.
*   Integrate Sentry for robust error tracking and reporting.
*   Configure OpenTelemetry to enable distributed tracing.


#### 1. Logging with Structlog

**Purpose:** Structured logging allows logs to be machine-readable (JSON) for easy search and aggregation.

* Logs contain fields like `method`, `handler`, `status`, and `duration`.
* Logs are output to console and can be aggregated in log management tools.

---

#### 2. Error Tracking with Sentry

**Purpose:** Capture exceptions and errors automatically.

* Requires `SENTRY_DSN` in environment variables.
* Middleware automatically captures exceptions from FastAPI endpoints.

---

#### 3. Metrics with Prometheus

**Purpose:** Measure system performance and usage (request counts, durations, status codes).

* Metrics are exposed via `/metrics` endpoint.
* Prometheus scrapes metrics and stores them.
* Metrics include request totals, duration sums and counts, and status code counts.

---

#### 4. Tracing with OpenTelemetry

**Purpose:** Track requests through the system to identify latency or errors.

* Spans represent individual requests and can be exported to tracing backends like Jaeger.
* Each HTTP request is wrapped in a span to visualize request flow and latency.

---

#### 5. Middleware for Request Logging & Audit

* Combines logging, tracing, and audit.
* Stores request info in the TinyDB audit table.
* Logs structured request information and wraps the request in OpenTelemetry spans.

---

#### 6. Grafana Dashboard

* Visualizes Prometheus metrics:

  1. HTTP Requests per Endpoint
  2. Request Duration
  3. HTTP Status Codes

* Ensure the time picker is set to the last 5–15 minutes to see live updates.

---

#### 7. How It Works Together

| Component     | Purpose                                                |
| ------------- | ------------------------------------------------------ |
| Structlog     | Structured logging for human + machine readability     |
| Sentry        | Automatic error reporting                              |
| Prometheus    | Collect request/latency metrics                        |
| Grafana       | Visualize metrics                                      |
| OpenTelemetry | Trace requests across services                         |
| Middleware    | Combines logging, tracing, and audit into each request |

* Logs show **what happened**.
* Metrics show **how often and how long**.
* Traces show **where latency occurs**.
* Error monitoring shows **unexpected failures**.

---

* Observability combines **logs, metrics, traces, and alerts**.
* Provides visibility into system health and user activity.
* Real-time metrics and dashboards help quickly identify issues.

## Milestone 2: User & Security

### Authentication & Access Control
*   Implement a simple one-click user creation feature for easy demonstration mode.
*   Develop JWT-based authentication for secure user logins.
*   Define a basic role model (`admin`, `physician`, `staff`) for access control.
*   Add audit trail logging for all actions related to patient records.

### Frontend Auth
*   Create a dedicated login page using Nuxt.js.
*   Use Pinia to manage and store the user authentication state.
*   Protect frontend routes, allowing access only based on user roles.

## Milestone 3: Patient Management

### Backend
*   Develop CRUD (Create, Read, Update, Delete) APIs for managing patient demographics and insurance information.
*   Establish a clear linkage between patients and their assigned physician.

### Frontend
*   Create a patient list view with search and filter capabilities.
*   Design a patient profile page to display demographics and insurance details.
*   Implement forms for editing and updating patient information.

## Milestone 4: Appointment Scheduling

### Backend
*   Develop APIs for creating, updating, and canceling appointments.
*   Implement logic for checking and preventing overlapping appointment times.

### Frontend
*   Integrate a visual calendar, using a library like Flowbite's date/time picker, for scheduling appointments.
*   Enable drag-and-drop functionality for easy rescheduling.
*   Create a modal window to display and edit appointment details.

## Milestone 5: Clinical Documentation

### Backend
*   Define the `Encounter` model to structure SOAP (Subjective, Objective, Assessment, Plan) notes.
*   Create an API for encounter note creation and retrieval.
*   Ensure versioning of notes to maintain an immutable history of clinical records.

### Frontend
*   Design an encounter entry form with the SOAP structure.
*   Implement a timeline view of past encounters on the patient's chart.

## Milestone 6: E-Prescribing

### Backend
*   Define the `Prescription` model.
*   Create an API to generate and "send" prescriptions. Start with a mock pharmacy integration.
*   Establish a link between prescriptions and their corresponding encounters.

### Frontend
*   Build a prescription form to capture drug details, dosage, route, and frequency.
*   Display a list of active versus past prescriptions on the patient chart.

## Milestone 7: Labs & Imaging

### Backend
*   Define the `LabOrder` model.
*   Create an API to order labs and "receive" mock lab results.
*   Implement storage for PDF or image-based lab results.

### Frontend
*   Add functionality to order labs directly from an encounter.
*   Develop a lab results viewer with a table for results and a file viewer for attached documents.

## Milestone 8: Billing

### Backend
*   Define the `BillingRecord` model.
*   Create an API to generate billing entries directly from an encounter.
*   Add functionality to assign CPT/ICD codes to billing records.

### Frontend
*   Create a billing dashboard to track pending versus paid invoices.
*   Implement an option to export invoices as PDF files.

## Milestone 9: Final Hardening

*   Perform comprehensive end-to-end testing across both the frontend and backend.
*   Refine and implement a robust, role-based access matrix.
*   Conduct a full security pass, including auditing logs and securing auth tokens.
*   Optimize TinyDB performance, including strategies for data archival and backups.
*   Create and refine performance dashboards in Grafana to monitor the live system.
