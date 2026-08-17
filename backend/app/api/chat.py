from typing import Annotated, Callable

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.dependencies import get_chat_service
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import EmptyMessageError, MessageTooShortError


router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


ChatService = Annotated[
    Callable[[str], str],
    Depends(get_chat_service),
]


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    chat_service: ChatService,
) -> ChatResponse:
    try:
        reply = chat_service(
            request.message,
        )
    except EmptyMessageError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    except MessageTooShortError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return ChatResponse(
        message=reply,
        model="echo",
        language=request.language,
    )