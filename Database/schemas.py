from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class SubjectBase(BaseModel):
    name: str


class Subject(SubjectBase):
    id: int

    class Config:
        orm_mode = True
