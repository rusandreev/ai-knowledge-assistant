from typing import Annotated, Callable

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.dependencies import get_chat_service_with_preview
from app.schemas.chat import ChatRequest, ChatPreviewResponse
from app.services.chat import EmptyMessageError, MessageTooShortError


router = APIRouter(
    prefix="/chat/preview",
    tags=["chat-preview"],
)


ChatPreviewService = Annotated[
    Callable[[str], str],
    Depends(get_chat_service_with_preview),
]


@router.post(
    "",
    response_model=ChatPreviewResponse,
)
async def chat(
    request: ChatRequest,
    chat_preview_service: ChatPreviewService,
) -> ChatPreviewResponse:
    try:
        reply = chat_preview_service(
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

    return build_metadata(reply, language=request.language)


def build_metadata(
    message: str,
    language: str | None = None,
) -> ChatPreviewResponse:
    metadata = {
        "length": len(message),
    }

    if language:
        metadata["language"] = language

    return ChatPreviewResponse(
        message=message,
        **metadata,
    )