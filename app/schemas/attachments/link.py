from pydantic import BaseModel

from app.schemas.attachments.photo import Photo
from app.schemas.auxilary_objects.button import ButtonAux
from app.schemas.auxilary_objects.product import ProductAux


class Link(BaseModel):
    url: str
    title: str
    description: str
    photo: Photo
    product: ProductAux
    button: ButtonAux
    preview_page: str
    preview_url: str
    