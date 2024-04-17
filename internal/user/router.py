from fastapi import APIRouter

from internal.user.schemas import *

router = APIRouter(prefix="/user", tags=["User operations"])


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    return User(**{
        "id": 5,
        "owner_id": 5,
        "title": user.title,
        "description": user.description
    })


@router.get("/", response_model=list[User])
def get_users():
    return [User(**{
        "id": 5,
        "owner_id": 5,
        "title": "TITLE",
        "description": "DESCRIPTION"
    })]


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    return User(**{
        "id": user_id,
        "owner_id": 5,
        "title": "TITLE",
        "description": "DESCRIPTION"
    })


@router.put("/", response_model=User)
def update_user(user: UserCreate):
    return User(**{
        "id": 5,
        "owner_id": 5,
        "title": "TITLE",
        "description": "DESCRIPTION"
    })
