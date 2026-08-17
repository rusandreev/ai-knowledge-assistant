class EmptyMessageError(ValueError):
    pass

class MessageTooShortError(ValueError):
    pass    

def create_echo_reply(message: str) -> str:
    clean_message = message.strip()

    if not clean_message:
        raise EmptyMessageError(
            "Message cannot contain only whitespace."
        )

    if len(clean_message) < 2:
        raise MessageTooShortError("Message is too short.")

    return f"You said: {clean_message}"

def create_chat_preview(message: str) -> str:
    clean_message = message.strip()

    if not clean_message:
        raise EmptyMessageError("Message cannot contain only whitespace.")

    if len(clean_message) < 2:
        raise MessageTooShortError("Message is too short.")

    return clean_message