from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


class Product(BaseModel):
    id: int
    name: str
    price: float
