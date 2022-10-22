from app.enums import UpdateType
from pydantic import BaseModel


class ClientInfo(BaseModel):
    pass


class MessageNew(BaseModel):
    message: Message
    client_info: ClientInfo


class Event(BaseModel):
    type: UpdateType
    event_id: str
    v: str
    object: MessageNew
    group_id: int


class Update(BaseModel):
    ts: int
    updates: list[Event]
    failed: int | None
