import json

import requests
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from internal.data.auth import pb_auth
from internal.data.database import get_db
from internal.user import service
from internal.user.schemas import *

router = APIRouter(prefix="/user", tags=["User operations"])


@router.post("/")
def create_user(user: UserCreateDto, db: Session = Depends(get_db), auth=Depends(pb_auth)):
    try:
        result = auth.create_user_with_email_and_password(user.email, user.password)
    except requests.exceptions.HTTPError as error:
        err = json.loads(error.args[1])["error"]
        raise HTTPException(status_code=err["code"], detail=err["message"])
    except Exception as error:
        raise internal_error(str(error))

    try:
        user = service.create_user(db, user)
    except Exception as error:
        raise internal_error(str(error))

    print("registered", user.email)
    return user


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


# Helpers

def internal_error(message: str):
    return HTTPException(status_code=500, detail=f"An internal server error occurred. Try again later." + str(message))
