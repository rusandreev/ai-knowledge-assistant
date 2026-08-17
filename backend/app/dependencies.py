from typing import Callable

from app.services.chat import create_echo_reply, create_chat_preview

def get_chat_service() -> Callable[[str], str]:
    return create_echo_reply

def get_chat_service_with_preview() -> Callable[[str], str]:
    return create_chat_preview