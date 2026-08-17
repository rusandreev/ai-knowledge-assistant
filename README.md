# AI Knowledge Assistant

A production-oriented AI application built step by step.

## Architecture

Next.js → FastAPI

## Current status

### Day 2

- [x] Typed request/response models
- [x] Pydantic validation
- [x] `POST /chat`
- [x] API router
- [x] service layer
- [x] basic error handling
- [x] frontend chat request
- [x] async/await experiment
- [x] first FastAPI dependency

### Day 1

- Next.js frontend
- FastAPI backend
- `/health` endpoint
- Frontend → backend request
- CORS configured

## Local development

Backend:

```bash
cd backend
fastapi dev app/main.py
```

Frontend:

```bash
cd frontend
npm run dev
```

Frontend: http://localhost:3000  
Backend: http://localhost:8000  
API docs: http://localhost:8000/docs