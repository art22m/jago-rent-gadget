from sqlalchemy.orm import Session

from internal.user import models
from internal.user.models import User
from internal.user.schemas import UserCreateDto, UserUpdateDto


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


def update_user(db: Session, user_update_dto: UserUpdateDto):
    user = get_user(db, user_id=user_update_dto.id)
    user.email = user_update_dto.email
    user.name = user_update_dto.name
    db.commit()


def create_user(db: Session, user: UserCreateDto):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
