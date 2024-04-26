from pydantic import BaseModel


class ItemCreateDto(BaseModel):
    title: str
    description: str | None = None
    s3_url: str
    price: int
    owner_id: int


class ItemUpdateDto(BaseModel):
    id: int
    title: str
    description: str | None = None
    s3_url: str
    price: int


class ItemDto(BaseModel):
    id: int
    title: str
    description: str | None = None
    s3_url: str
    price: int
    owner_id: int

    class Config:
        orm_mode = True
