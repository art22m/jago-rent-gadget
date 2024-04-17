from fastapi import APIRouter

from internal.item.schemas import *

router = APIRouter(prefix="/item", tags=["Item operations"])


@router.post("/", response_model=Item)
def create_item(item: ItemCreate):
    return Item(**{
        "id": 5,
        "owner_id": 5,
        "title": item.title,
        "description": item.description
    })


@router.get("/", response_model=list[Item])
def get_items():
    return [Item(**{
        "id": 5,
        "owner_id": 5,
        "title": "TITLE",
        "description": "DESCRIPTION"
    })]


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    return Item(**{
        "id": item_id,
        "owner_id": 5,
        "title": "TITLE",
        "description": "DESCRIPTION"
    })


@router.put("/", response_model=Item)
def update_item(item: ItemCreate):
    return Item(**{
        "id": 5,
        "owner_id": 5,
        "title": "TITLE",
        "description": "DESCRIPTION"
    })
