# ETL Guard

A full-stack ETL monitoring and data quality platform that allows users to upload CSV datasets, validate dirty data, clean datasets automatically, detect schema drift, and monitor upload analytics through an interactive dashboard.

## Live Demo

Frontend (Vercel):  
https://etl-guard.vercel.app/

Backend API (Render):  
https://etl-guard.onrender.com

Backend Swagger Docs:  
https://etl-guard.onrender.com/docs

---

# Features

## Authentication System
- User Signup and Login
- JWT-based Authentication
- Protected API Routes
- User-specific Upload History and Analytics

## CSV Upload & Processing
- Upload CSV datasets
- Preview uploaded raw dataset
- Download cleaned CSV files

## Data Validation Engine
Detects:
- Missing values
- Duplicate rows
- Invalid email formats
- Negative numeric values

## Data Cleaning Pipeline
Automatically:
- Removes duplicates
- Fills missing values
- Fixes invalid emails
- Cleans numeric inconsistencies
- Standardizes dataset formatting

## Schema Drift Detection
Compares uploaded dataset schema against expected schema and detects:
- Missing columns
- Extra columns
- Datatype mismatches

## Analytics Dashboard
Displays:
- Total uploads
- Total rows processed
- Upload history
- Interactive charts and analytics

## Cloud Deployment
- Frontend deployed on Vercel
- Backend deployed on Render
- PostgreSQL database hosted on Neon

## Dockerized Architecture
- Docker support for frontend, backend, and database
- Docker Compose orchestration

---

# Tech Stack

## Frontend
- React.js
- Bootstrap
- Axios
- Recharts

## Backend
- FastAPI
- Python
- SQLAlchemy
- JWT Authentication
- Pandas

## Database
- PostgreSQL

## DevOps & Deployment
- Docker
- Docker Compose
- Vercel
- Render
- Neon PostgreSQL

---

# Project Architecture

```text
React Frontend (Vercel)
        ↓
FastAPI Backend (Render)
        ↓
PostgreSQL Database (Neon)
