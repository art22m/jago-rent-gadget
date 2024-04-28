from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json
import pyrebase
from internal.data.database import SessionLocal
from internal.user import service
from internal.user.schemas import *

pb_auth = pyrebase.initialize_app(
    json.load(open("./configs/firebase-pyrebase.json"))
).auth()

router = APIRouter(prefix="/user", tags=["User operations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_user(user: UserCreateDto, db: Session = Depends(get_db)):
    try:
        result = pb_auth.create_user_with_email_and_password(user.email, user.password)
    except Exception as e:
        return e

    try:
        service.create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An internal server error occurred. Try again later." + str(e))

    return result


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
