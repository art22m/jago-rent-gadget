from fastapi import APIRouter

import schemas

router = APIRouter()


@router.post("/users", response_model=schemas.Item)
def create_user(item: schemas.ItemCreate):
    return schemas.Item(**{
        "id": 5,
        "owner_id": 5,
        "title": item.title,
        "description": item.description
    })


@router.get("/users", response_model=schemas.Item)
def get_users():
    return schemas.Item(**{
        "id": 5,
        "owner_id": 5,
        "title": "TITLE",
        "description": "DESCRIPTION"
    })
