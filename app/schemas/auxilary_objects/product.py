from pydantic import BaseModel


class PriceAux(BaseModel):
    amount: int
    currency: Item
    text: str


class ProductAux(BaseModel):
    price: PriceAux
