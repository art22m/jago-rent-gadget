from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from internal.data.auth import pb_auth
from internal.data.database import get_db
from internal.user import service
from internal.user.schemas import (UserCreateDto, UserDto, UserSigninDto,
                                   UserUpdateDto)

router = APIRouter(prefix="/user", tags=["User operations"])


@router.post("/")
def create_user(
    user: UserCreateDto, db: Session = Depends(get_db), auth=Depends(pb_auth)
):
    return service.create_user(db, auth, user)


@router.get("/signin")
def signin_user(
    user: UserSigninDto, db: Session = Depends(get_db), auth=Depends(pb_auth)
):
    return service.signin_user(db, auth, user)


@router.get("/", response_model=list[UserDto])
def get_users(db: Session = Depends(get_db)):
    return service.get_users(db)


@router.get("/{user_id}", response_model=UserDto)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user(db, user_id=user_id)


@router.get("/by-email/{email}", response_model=UserDto)
def get_user_email(email: str, db: Session = Depends(get_db)):
    return service.get_user_by_email(db, email=email)


@router.put("/", response_model=UserDto)
def update_user(user: UserUpdateDto, db: Session = Depends(get_db)):
    return service.update_user(db, user_update_dto=user)
