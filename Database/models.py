from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
