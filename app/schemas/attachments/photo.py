from pydantic import BaseModel


class PhotoSize(BaseModel):
    url: str
    width: int
    height: int
    type: str


class Photo(BaseModel):
    id: int
    album_id: int
    owner_id: int
    user_id: int
    text: str
    sizes: list[PhotoSize]
    width: int
    height: int
