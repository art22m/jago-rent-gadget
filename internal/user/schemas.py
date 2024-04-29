from pydantic import BaseModel

from internal.item.schemas import ItemDto


class UserCreateDto(BaseModel):
    email: str
    password: str
    name: str


class UserSigninDto(BaseModel):
    email: str
    password: str


class UserUpdateDto(BaseModel):
    id: int
    email: str
    name: str


class UserDto(BaseModel):
    id: int
    email: str
    name: str
    items: list[ItemDto] = []

    class Config:
        from_attributes = True
