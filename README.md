# AI API Failure Debugger

An AI-powered developer tool that analyzes API failures, detects probable causes, calculates confidence scores, and generates debugging insights using FastAPI, React, PostgreSQL, and OpenAI.

---

# Features

- AI-powered API error analysis
- Smart error pattern detection
- Confidence score calculation
- Root cause identification
- Suggested debugging solutions
- PostgreSQL database integration
- Modern dashboard UI
- FastAPI backend architecture
- React frontend with Tailwind CSS

---

# Tech Stack

## Frontend
- React
- Vite
- Tailwind CSS
- Axios

## Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL

## AI
- OpenAI API

---

# Project Architecture

Frontend (React)
↓
FastAPI Backend
↓
Validation Layer
↓
Pattern Detection Engine
↓
Confidence Scoring System
↓
AI Explanation Engine
↓
PostgreSQL Database

---

# Folder Structure

```bash
ai-api-debugger/
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── main.py
│   ├── database.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
```

---

# Backend Setup

```bash
cd backend
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

## Mac/Linux

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create database:

```sql
CREATE DATABASE api_debugger;
```

Update database connection inside:

```bash
backend/database.py
```

Example:

```python
DATABASE_URL = "postgresql://username@localhost/api_debugger"
```

---

# Environment Variables

Create `.env` file inside backend:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# API Endpoint

## Analyze API Error

### POST `/analyze`

Request:

```json
{
  "api_name": "OpenAI",
  "error_message": "429 Too Many Requests"
}
```

Response:

```json
{
  "category": "Rate Limiting",
  "cause": "Too many requests in short time",
  "solutions": [
    "Use retry logic",
    "Reduce request frequency"
  ],
  "confidence_score": "75%",
  "ai_explanation": "..."
}
```

---

# Future Improvements

- Error history dashboard
- Authentication system
- Docker deployment
- Advanced AI reasoning
- Log file upload support
- Multi-model AI support

---

# Learning Outcomes

This project helped in understanding:

- REST API development
- Backend architecture
- AI integration workflows
- PostgreSQL database management
- ORM with SQLAlchemy
- React frontend development
- Prompt engineering
- Error handling systems
- Full stack system design

---

# Author

Anuman Shailesh Modi