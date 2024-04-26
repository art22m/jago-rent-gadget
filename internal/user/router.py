from fastapi import APIRouter, Depends, HTTPException
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
    if service.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail=f"User with email={user.email} is already exists")
    return service.create_user(db, user)


@router.get("/", response_model=list[UserDto])
def get_users(db: Session = Depends(get_db)):
    return service.get_users(db)


@router.get("/{user_id}", response_model=UserDto)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user(db, user_id=user_id)


@router.get("/by-email/{email}", response_model=UserDto)
def get_user(email: str, db: Session = Depends(get_db)):
    return service.get_user_by_email(db, email=email)


@router.put("/", response_model=UserDto)
def update_user(user: UserUpdateDto, db: Session = Depends(get_db)):
    return service.update_user(db, user_update_dto=user)
