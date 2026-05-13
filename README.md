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

```
React Frontend (Vercel)
        ↓
FastAPI Backend (Render)
        ↓
PostgreSQL Database (Neon)
```

# Installation & Local Setup

## Clone Repository

```bash
git clone https://github.com/your-username/etl-guard.git

cd etl-guard
```

---

# Backend Setup

## Navigate to Backend

```bash
cd backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend will run on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## Navigate to Frontend

```bash
cd frontend
```

## Install Frontend Dependencies

```bash
npm install
```

---

## Create Environment Variable File

Create a `.env` file inside the `frontend` folder.

Add:

```env
REACT_APP_API_URL=http://127.0.0.1:8000
```

---

## Run React Frontend

```bash
npm start
```

Frontend will run on:

```text
http://localhost:3000
```

---

# Docker Setup

## Run Full Application with Docker

From the root project folder:

```bash
docker compose up --build
```

---

## Run Docker in Background

```bash
docker compose up -d
```

---

## Stop Docker Containers

```bash
docker compose down
```

---

# Production Deployment

## Frontend Deployment

Frontend deployed using Vercel:

```text
https://your-vercel-app.vercel.app
```

---

## Backend Deployment

Backend deployed using Render:

```text
https://etl-guard.onrender.com
```

---

## Database Hosting

PostgreSQL database hosted on Neon.

---

# Environment Variables

## Frontend `.env`

```env
REACT_APP_API_URL=https://etl-guard.onrender.com
```

---

# API Endpoints

## Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/signup` | Register a new user |
| POST | `/login` | Login existing user |

---

## ETL APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/upload` | Upload CSV dataset |
| GET | `/download/{filename}` | Download cleaned CSV |

---

## Dashboard APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/uploads` | Fetch upload history |
| GET | `/analytics` | Fetch analytics summary |

---

# Sample Test Datasets

Datasets used for testing:

- Dirty Cafe Sales Dataset(kaggle)
- Employee Dirty Dataset(kaggle)

# Future Improvements

- Real-time ETL monitoring
- Apache Airflow integration
- Machine learning based anomaly detection
- Export reports in PDF/Excel format
- Email notifications for failed uploads
- Support for Excel and JSON datasets
- CI/CD pipeline integration
- Kubernetes deployment support

---

# Author

## Ankita Dash

GitHub:  
https://github.com/Kite020

LinkedIn:  
https://www.linkedin.com/in/ankita-dash-3377b1245/

---

# License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2026 Ankita Dash

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

