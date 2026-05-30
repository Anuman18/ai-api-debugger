# AI API Failure Debugger

An AI-powered developer tool that analyzes API failures, detects probable root causes, calculates confidence scores, and generates intelligent debugging insights using FastAPI, React, PostgreSQL, and OpenAI.

---

## Live Demo

### Frontend

https://ai-api-debugger-nu.vercel.app/

### Backend API Docs

https://ai-api-debugger-jrmm.onrender.com/docs

---

## Features

* AI-powered API error analysis
* Intelligent error pattern detection
* Confidence score calculation
* Root cause identification
* Suggested debugging solutions
* OpenAI-powered debugging explanations
* PostgreSQL database integration
* Modern dashboard UI
* FastAPI backend architecture
* Cloud deployment with Render, Neon, and Vercel

---

## Dashboard Preview

> Add screenshots here

### Main Dashboard

```text
assets/dashboard.png
```

### Analysis Result

```text
assets/result.png
```

### Swagger API Documentation

```text
assets/swagger.png
```

---

## Problem Statement

Developers often spend significant time debugging API failures such as authentication errors, rate limiting issues, timeout problems, and server-side failures.

Traditional debugging requires manually analyzing logs, documentation, and error messages.

This project provides an AI-powered debugging assistant that automatically analyzes API failures, identifies probable causes, calculates confidence scores, and suggests troubleshooting strategies.

---

## Solution

The system combines:

* Rule-based error classification
* Pattern matching engine
* Confidence scoring system
* AI-enhanced debugging explanations
* Persistent PostgreSQL storage

to create a developer-focused debugging platform.

---

## Tech Stack

### Frontend

* React
* Vite
* Tailwind CSS
* Axios

### Backend

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL

### AI Integration

* OpenAI API

### Deployment

* Vercel
* Render
* Neon PostgreSQL

---

## System Architecture

```text
React Frontend
       ↓
FastAPI Backend
       ↓
Validation Layer
       ↓
Pattern Detection Engine
       ↓
Confidence Scoring System
       ↓
OpenAI API
       ↓
PostgreSQL Database
```

---

## Project Structure

```bash
ai-api-debugger/
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── database.py
│   ├── main.py
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

## API Endpoint

### Analyze Error

**POST**

```http
/analyze
```

### Request

```json
{
  "api_name": "OpenAI",
  "error_message": "429 Too Many Requests"
}
```

### Response

```json
{
  "category": "Rate Limiting",
  "cause": "Too many requests in short time",
  "solutions": [
    "Use retry logic",
    "Reduce request frequency",
    "Add exponential backoff"
  ],
  "confidence_score": "75%",
  "ai_explanation": "Detailed AI-generated debugging explanation..."
}
```

---

## Key Engineering Concepts Implemented

* REST API Development
* Backend Architecture Design
* Layered Service Structure
* Rule-Based Classification Engine
* AI Integration Workflows
* PostgreSQL Database Management
* ORM with SQLAlchemy
* Cloud Deployment
* Environment Variable Management
* CORS Handling
* Production Debugging

---

## Challenges Solved

* API error classification
* OpenAI integration
* Database persistence
* Cross-origin request handling (CORS)
* Cloud deployment configuration
* Environment variable management
* Production debugging

---

## Future Improvements

* Authentication System
* User Accounts
* Error History Dashboard
* Log File Upload Support
* Docker Deployment
* Advanced AI Reasoning
* Analytics Dashboard
* Multi-Model AI Support

---

## Learning Outcomes

This project helped in understanding:

* Full Stack Development
* Backend Engineering
* FastAPI Development
* React Frontend Architecture
* PostgreSQL Integration
* AI-Powered Applications
* Cloud Deployment
* System Design Fundamentals
* Production-Level Debugging

---

## Author

### Anuman Shailesh Modi

Artificial Intelligence & Data Science Student

GitHub:
https://github.com/Anuman18

LinkedIn:
Add your LinkedIn profile link here
