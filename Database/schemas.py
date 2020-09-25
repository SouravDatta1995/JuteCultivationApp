from datetime import datetime

from pydantic import BaseModel


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
    dateofsowing: datetime
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

    class Config:
        orm_mode = True


class JuteSurveyInput(JuteSurveyInputBase):
    id: int

    class Config:
        orm_mode = True
