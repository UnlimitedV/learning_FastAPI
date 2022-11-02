from pydantic import BaseModel


class BlogModel(BaseModel):
    title: str
    text: str
    published: bool | None = None
