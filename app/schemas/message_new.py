from pydantic import BaseModel

class Message(BaseModel):
    id: int
    date: int
    peer_id: int
    from_id: int
    text: str
    random_id: int
    ref: str
    ref_source: str
    attachments: list[...]
    important: bool
    geo: Geography
    payload: str
    keyboard: ...
    fwd_messages: list[...]
    reply_message: ...
