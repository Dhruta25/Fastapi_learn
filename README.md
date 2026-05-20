# Employee Management API

A simple backend CRUD API built using FastAPI, SQLAlchemy, and SQLite.

This project helps beginners understand:
- FastAPI basics
- REST API structure
- CRUD operations
- Database connection
- SQLAlchemy ORM
- Project folder structure

---

# Features

- Create Employee
- Get All Employees
- Get Single Employee
- Update Employee
- Delete Employee
- SQLite Database Integration
- SQLAlchemy ORM
- Automatic Swagger API Docs

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| FastAPI | Backend Framework |
| SQLite | Database |
| SQLAlchemy | ORM for database operations |
| Uvicorn | ASGI server |

---

# Project Structure

```bash
project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   └── routes/
│       └── employee.py
│
├── employee.db
├── requirements.txt
└── README.md
```

---

# File Explanation

## main.py

Application entry point.

Responsible for:
- starting FastAPI app
- creating database tables
- including API routes

---

## database.py

Handles database connection.

Responsible for:
- creating SQLite engine
- creating database session
- creating Base class for models

---

## models.py

Defines database tables using SQLAlchemy.

Example:
- Employee table
- columns like id, name, age, salary

---

## schemas.py

Defines request and response validation using Pydantic.

Responsible for:
- validating API input
- formatting API output

---

## routes/employee.py

Contains all API endpoints.

Responsible for:
- CRUD operations
- database queries
- error handling

---

# Installation

## Clone Repository

```bash
git clone <your-repository-link>
```

---

## Move Into Project Folder

```bash
cd project
```

---

## Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

---

# Run Server

```bash
uvicorn app.main:app --reload
```

---

# Open Swagger Documentation

After running server open:

```text
http://127.0.0.1:8000/docs
```

You can:
- test APIs
- send requests
- view responses
- understand request body formats

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/employees/` | Create employee |
| GET | `/employees/` | Get all employees |
| GET | `/employees/{employee_id}` | Get single employee |
| PUT | `/employees/{employee_id}` | Update employee |
| DELETE | `/employees/{employee_id}` | Delete employee |

---

# Example Request Body

```json
{
  "name": "Dhruta",
  "age": 20,
  "salary": 50000
}
```

---

# How Data Flows

```text
Client Request
      ↓
FastAPI Route
      ↓
Pydantic Schema Validation
      ↓
SQLAlchemy Model
      ↓
Database Session
      ↓
SQLite Database
```

---

# CRUD Operations Explained

## Create

Adds new employee into database.

---

## Read

Fetches employee data from database.

---

## Update

Modifies existing employee details.

---

## Delete

Removes employee from database.

---

# Database Used

This project uses SQLite database.

Database file:

```text
employee.db
```

All employee data is stored inside this file.

---

# ORM Used

This project uses SQLAlchemy ORM.

SQLAlchemy helps interact with database using Python code instead of writing raw SQL queries.

---

# Learning Outcomes

After completing this project you will understand:
- FastAPI routing
- HTTP methods
- Path parameters
- Pydantic validation
- SQLAlchemy ORM
- Database sessions
- CRUD operations
- REST API structure
- Backend project architecture

---

# Future Improvements

Possible future upgrades:
- JWT Authentication
- Password Hashing
- PostgreSQL Integration
- Docker Support
- Async Database
- Pagination
- Search & Filtering
- Role-Based Authentication

---

# Author

Dhrutabrata Biswal