from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from internal import utils
from internal.data.database import get_db
from internal.item import service
from internal.item.schemas import ItemCreateDto, ItemDto, ItemUpdateDto
from internal.user.service import get_user

router = APIRouter(prefix="/item", tags=["Item operations"])


@router.post(
    "/",
    dependencies=[Depends(utils.validate_firebase)],
    response_model=ItemDto,
)
def create_item(item: ItemCreateDto, db: Session = Depends(get_db)):
    get_user(db, item.owner_id)
    return service.create_item(db, item)


@router.get("/", response_model=list[ItemDto])
def get_items(db: Session = Depends(get_db)):
    return service.get_items(db)


@router.get("/user/{user_id}", response_model=list[ItemDto])
def get_items_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_items_by_user(db, user_id)


@router.get("/{item_id}", response_model=ItemDto)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return service.get_item(db, item_id)


@router.put(
    "/",
    dependencies=[Depends(utils.validate_firebase)],
    response_model=ItemDto,
)
def update_item(item: ItemUpdateDto, db: Session = Depends(get_db)):
    return service.update_item(db, item)


@router.delete(
    "/{item_id}",
    dependencies=[Depends(utils.validate_firebase)],
    response_model=bool,
)
def delete_item(item_id, db: Session = Depends(get_db)):
    return service.delete_item(db, item_id)
