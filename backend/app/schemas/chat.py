from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=4000,
    )
    language: str | None = None
    conversation_id: str | None = None

class ChatResponse(BaseModel):
    message: str
    model: str
    language: str | None = None

class ChatPreviewResponse(BaseModel):
    message: str
    length: int
    language: str | None = None