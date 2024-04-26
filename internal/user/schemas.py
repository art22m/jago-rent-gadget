from pydantic import BaseModel

from internal.item.schemas import Item


class UserCreateDto(BaseModel):
    email: str
    name: str


class UserUpdateDto(BaseModel):
    id: int
    email: str
    name: str


class UserDto(BaseModel):
    id: int
    email: str
    name: str
    items: list[Item] = []

    class Config:
        orm_mode = True
