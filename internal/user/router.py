from fastapi import APIRouter, Depends
from internal.user.schemas import *
import internal.utils

router = APIRouter(prefix="/user", tags=["User operations"])


@router.get("/test")
async def test(user=Depends(internal.utils.validate_firebase)):
    """Test endpoint that depends on authenticated firebase"""
    print(user)
    return user


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    return User(
        **{"id": 5, "owner_id": 5, "title": user.title, "description": user.description}
    )


@router.get("/", response_model=list[User])
def get_users():
    return [
        User(**{"id": 5, "owner_id": 5, "title": "TITLE", "description": "DESCRIPTION"})
    ]


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    return User(
        **{"id": user_id, "owner_id": 5, "title": "TITLE", "description": "DESCRIPTION"}
    )


@router.put("/", response_model=User)
def update_user(user: UserCreate):
    return User(
        **{"id": 5, "owner_id": 5, "title": "TITLE", "description": "DESCRIPTION"}
    )
