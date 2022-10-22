from pydantic import BaseModel


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class Geography(BaseModel):
    type: str
    coordinates: list[Coordinate]
