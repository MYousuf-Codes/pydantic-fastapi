from pydantic import BaseModel

# TODO: Create a Product model with id, name, price, and in_stock fields

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

