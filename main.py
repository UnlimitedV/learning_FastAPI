from fastapi import FastAPI

from typing import Optional
from enum import Enum


app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {f"{limit} published blogs from db"}
    else:
        return {f"{limit} unpublished blogs from db"}


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
    product = "product"
    colection = "colection"
    category = "category"


@app.get("/model/{model_name}")
def get_model(model_name: ModelName):
    return {f"model_name is {model_name}"}
