from pydantic import BaseModel

from app.schemas.auxilary_objects.product import PriceAux


class Price(PriceAux):
    old_amount: str


class ProductDimension(BaseModel):
    width: int
    height: int
    length: int


class ProductCategory(BaseModel):
    id: int
    name: str
    section: Item


class Product(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str
    price: Price
    dimensions: ProductDimension
    weight: int
    category: ProductCategory
    thumb_photo: str
    date: int
    availability: int
    