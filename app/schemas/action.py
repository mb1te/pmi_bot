from pydantic import BaseModel
from strenum import StrEnum

from app.schemas.attachments import Cover


class ActionType(StrEnum):
    ChatPhotoUpdate = "chat_photo_update"
    ChatPhotoRemove = "chat_photo_remove"
    ChatCreate = "chat_create"
    ChatTitleUpdate = "chat_title_update"
    ChatInviteUser = "chat_invite_user"
    ChatKickUser = "chat_kick_user"
    ChatPinMessage = "chat_pin_message"
    ChatUnpinMessage = "chat_unpin_message"
    ChatInviteUserByLink = "chat_invite_user_by_link"


class Action(BaseModel):
    type: ActionType
    member_id: int | None
    text: str | None
    email: str | None
    photo: Cover
