from pydantic import BaseModel, Field


class BlogModel(BaseModel):
    title: str
    text: str
    published: bool | None = None


class Item(BaseModel):
    name: str
    description: str = Field(
        default=None, title="the discription of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None
