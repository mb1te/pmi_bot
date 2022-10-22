from enum import IntEnum
from pydantic import BaseModel

from app.schemas.attachments.photo import PhotoSize


class FileType(IntEnum):
    TEXT = 1
    ARCHIVE = 2
    GIF = 3
    IMAGE = 4
    AUDIO = 5
    VIDEO = 6
    BOOK = 7
    UNKNOWN = 8


class PhotoPreview(BaseModel):
    sizes: list[PhotoSize]


class Graffiti(BaseModel):
    src: str
    width: int
    height: int


class AudioMessage(BaseModel):
    duration: int
    waveform: list[int]
    link_ogg: str
    link_mp3: str


class FilePreview(BaseModel):
    photo: PhotoPreview
    graffiti: Graffiti
    audio_message: AudioMessage


class File(BaseModel):
    id: int
    owner_id: int
    title: str
    size: int
    ext: str
    url: str
    date: int
    type: FileType
    preview: FilePreview
