from fastapi import HTTPException
from sqlalchemy.orm import Session

from internal.item import models
from internal.item.models import Item
from internal.item.schemas import ItemCreateDto, ItemUpdateDto
from internal.user.service import get_user


def get_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} is not found")
    return item


def get_items_by_user(db: Session, user_id: int):
    get_user(db, user_id)
    return db.query(Item).filter(Item.owner_id == user_id).all()


def get_items(db: Session):
    return db.query(Item).all()


def update_item(db: Session, item_update_dto: ItemUpdateDto):
    item = get_item(db, item_update_dto.id)
    item.title = item_update_dto.title
    item.description = item_update_dto.description
    item.price = item_update_dto.price
    item.s3_url = item.s3_url
    db.refresh(item)
    db.commit()
    return item


def delete_item(db: Session, item_id: int):
    db.delete(get_item(db, item_id))
    db.commit()
    return True


def create_item(db: Session, item_create_dto: ItemCreateDto):
    db_user = models.Item(
        title=item_create_dto.title,
        description=item_create_dto.description,
        s3_url=item_create_dto.s3_url,
        price=item_create_dto.price,
        owner_id=item_create_dto.owner_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
