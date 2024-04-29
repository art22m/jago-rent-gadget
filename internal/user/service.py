import json

import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session

from internal.user import models
from internal.user.models import User
from internal.user.schemas import UserCreateDto, UserUpdateDto


def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id={user_id} is not found")
    return user


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with email={email} is not found")
    return user


def get_users(db: Session):
    return db.query(User).all()


def update_user(db: Session, user_update_dto: UserUpdateDto):
    user = get_user(db, user_id=user_update_dto.id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id={user.id} is not found")
    user.email = user_update_dto.email
    user.name = user_update_dto.name
    db.commit()
    return get_user(db, user.id)


def create_user(db: Session, auth, user: UserCreateDto):
    try:
        result = auth.create_user_with_email_and_password(user.email, user.password)
    except requests.exceptions.HTTPError as error:
        err = json.loads(error.args[1])["error"]
        raise HTTPException(status_code=err["code"], detail=err["message"])
    except Exception as error:
        raise internal_error(str(error))

    try:
        db_user = models.User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as error:
        raise internal_error(str(error))

    print("registered", user.email)
    # TODO: переделать. Надо, что при создании сущности возвращался ее id'шник
    return db_user


def internal_error(message: str):
    return HTTPException(status_code=500, detail=f"An internal server error occurred. Try again later." + str(message))
