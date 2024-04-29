from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from internal.data.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    items = relationship("Item", back_populates="owner")
