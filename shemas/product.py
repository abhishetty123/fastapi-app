from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    price: float
    category: str
    qty: int

class ProductUpdateSchema(BaseModel):
    name: str | None = None
    price: float | None = None
    category: str | None = None
    qty: int | None = None
