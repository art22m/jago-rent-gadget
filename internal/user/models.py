from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from internal.data.database import Base
from internal.item.models import Item  # noqa # pylint: disable=unused-import


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    items = relationship("Item", back_populates="owner")
