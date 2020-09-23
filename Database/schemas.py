from datetime import datetime

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


class JuteSurveyInputBase(BaseModel):
    name: str
    plot: str
    plotarea: int
    soiltype: str
    soilhealthcard: bool
    nitrogenamount: float
    phosphorousamount: float
    pottasiumamount: float
    organiccarbonamount: float
    dateofsowing: float
    methodofsowing: int
    varietyused: int
    methodofweeding: int
    amountofseed: int
    dateofharvest: datetime
    daysleftforharvest: int
    methodofretting: int
    sourceofwater: int
    availabilityofwater: bool
    qualityofwashingwater: bool
    daysrequiredforcompleteretting: str
    rainfall: float
    temperature: str
    humidity: str


class JuteSurveyInput(JuteSurveyInputBase):
    id: int

    class Config:
        orm_mode = True
