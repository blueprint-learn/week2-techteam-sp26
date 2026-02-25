from pydantic import BaseModel


class User(BaseModel):
    _id: int
    name: str
    email: str


class Product(BaseModel):
    _id: int
    name: str
    price: float
