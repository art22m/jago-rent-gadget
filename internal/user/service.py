from fastapi import HTTPException
from sqlalchemy.orm import Session

from internal.user import models
from internal.user.models import User
from internal.user.schemas import UserCreateDto, UserUpdateDto, UserDto


def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return user


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_users(db: Session):
    return db.query(User).all()


def update_user(db: Session, user_update_dto: UserUpdateDto):
    user = get_user(db, user_id=user_update_dto.id)
    user.email = user_update_dto.email
    user.name = user_update_dto.name
    db.refresh(user)
    db.commit()
    return user


def create_user(db: Session, user: UserCreateDto):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
