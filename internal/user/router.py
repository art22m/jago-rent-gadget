from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from internal.data.database import SessionLocal
from internal.user import service
from internal.user.schemas import *

router = APIRouter(prefix="/user", tags=["User operations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserDto)
def create_user(user: UserCreateDto, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/", response_model=list[UserDto])
def get_users(db: Session = Depends(get_db)):
    return service.get_users(db)


@router.get("/{user_id}", response_model=UserDto)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user(db, user_id=user_id)


@router.put("/", response_model=UserDto)
def update_user(user: UserUpdateDto, db: Session = Depends(get_db)):
    service.update_user(db, user_update_dto=user)
