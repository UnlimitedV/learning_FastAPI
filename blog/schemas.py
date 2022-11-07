from pydantic import BaseModel, Field, HttpUrl, EmailStr


class BlogModel(BaseModel):
    title: str
    text: str
    published: bool | None = None


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str = Field(
        default=None, title="the discription of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str
