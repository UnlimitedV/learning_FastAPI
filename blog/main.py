from fastapi import FastAPI, Query, Path, Body, Cookie, Header, Form

from typing import Optional
from enum import Enum
from datetime import datetime, time, timedelta
from uuid import UUID

from .schemas import BlogModel, Item, Offer, Image, UserIn, UserOut, UserInDB


app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {f"{limit} published blogs from db"}
    else:
        return {f"{limit} unpublished blogs from db"}


@app.post("/blog")
def create_blog(blog: BlogModel):
    return {"data": f"blog created with title as '{blog.title}'"}


@app.get("/blog/unpublished")
def unpublished():
    # return all unpublished blogs
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {"blog": id}


@app.get("/blog/{id}/comments")
def comments(id):
    # fetch coments for blog with id = id
    return {"data": {"1", "2"}}


class ModelName(str, Enum):
    blog = "blog"
    comments = "comments"
    authors = "authors"


@app.get("/model/{model_name}")
def get_model(model_name: ModelName):
    return {f"model_name is {model_name}"}


@app.get("/items/{item_id}")
def read_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(
    item_id: UUID,
    start_datetime: datetime | None = Body(default=None),
    end_datetime: datetime | None = Body(default=None),
    repeat_at: time | None = Body(default=None),
    process_after: timedelta | None = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


@app.post("/images/multiple/")
def create_multiple_images(images: list[Image]):
    return {"images": images}


@app.post("/offer")
def create_offers(offer: Offer = Body(embed=True)):
    return {"offer": offer}


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights


@app.get("/items/")
async def read_items(
    ads_id: str | None = Cookie(default=None),
    user_agent: str | None = Header(default=None),
):
    return {"ads_id": ads_id, "User-Agent": user_agent}


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


@app.post("/login/")
def login(username: str = Form(), password: str = Form()):
    return {"username": username}
