from pydantic import BaseModel


class Cover(BaseModel):
    photo_50: str
    photo_100: str
    photo_200: str


class Image(BaseModel):
    height: int
    width: int
    url: str
    with_padding: int | None


