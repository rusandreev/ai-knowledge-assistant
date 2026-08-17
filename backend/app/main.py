from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.chat_preview import router as chat_preview_router

app = FastAPI(
    title="AI Knowledge Assistant API",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "AI Knowledge Assistant API",
        "version": "0.2.0",
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "ai-knowledge-assistant"
    }

app.include_router(chat_router)
app.include_router(chat_preview_router)