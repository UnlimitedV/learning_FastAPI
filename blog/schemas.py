from pydantic import BaseModel


class BlogModel(BaseModel):
    title: str
    text: str
    published: bool | None = None


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None
