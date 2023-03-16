from sqlalchemy import Column, BIGINT, FLOAT

from .base import Base


class User(Base):
    id = Column(BIGINT, primary_key=True)
    lat = Column(FLOAT, nullable=True)
    lon = Column(FLOAT, nullable=True)
