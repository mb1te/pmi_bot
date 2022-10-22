from pydantic import BaseModel


class Audio(BaseModel):
    id: int
    owner_id: int
    artist: str
    title: str
    duration: int
    url: str
    lyrics_id: int
    album_id: int
    genre_id: int
    date: int
    no_search: int
    is_hq: int
