# AIRA Data Platform

A backend data platform built using FastAPI, PostgreSQL, SQLAlchemy, and Alembic.

This project was created as part of the AIRA technical challenge to demonstrate backend API development, database design, migrations and clean project structuring.

---

# Project Overview

The platform provides:

- Tenant management
- User management
- PostgreSQL database integration
- Alembic database migrations
- FastAPI REST APIs
- Swagger API documentation

---

# Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Uvicorn

---

# Project Structure

aira-data-platform/
│── app/
│   │── api/
│   │── core/
│   │── db/
│   │── models/
│   │── schemas/
│   │── services/
│
│── alembic/
│── alembic.ini
│── main.py
│── requirements.txt
│── README.md

---

# Setup Instructions

## 1. Clone Repository

git clone <your-github-repo-url>

cd aira-data-platform

---

## 2. Create Virtual Environment

python -m venv venv

Activate:

venv\Scripts\activate

---

## 3. Install Dependencies

pip install -r requirements.txt

---

## 4. PostgreSQL Database

Create database:

aira_db

---

## 5. Configure Database URL

Inside config file:

DATABASE_URL = "postgresql://postgres:<your-password>@localhost:5432/aira_db"

---

## 6. Run Alembic Migration

alembic upgrade head

---

## 7. Run Application

uvicorn main:app --reload

---

# API Access

Swagger UI:

http://127.0.0.1:8000/docs

---

# Current API

## Health Check

GET /

Response:

{
  "message": "AIRA Data Platform Running"
}

---

# Database Design

Current schema includes:

## tenant

- id
- name
- created_at

## user

- id
- email
- role
- tenant_id

---

# Migration Handling

Alembic is used for:

- schema versioning
- database upgrades
- repeatable migrations

---

# Assumptions

- Local PostgreSQL installation is used
- Single environment setup
- Initial schema only

---

# Future Improvements

- JWT Authentication
- Role-based Access Control
- Logging
- Testing
- Docker Support
- CI/CD Pipeline

---
