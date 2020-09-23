from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime

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


class JuteSurveyInputs(Base):
    __tablename__ = "jutesurveyinputs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    plot = Column(String, nullable=False)
    plotarea = Column(Integer, nullable=False)
    soiltype = Column(String)
    soilhealthcard = Column(Boolean)
    nitrogenamount = Column(Numeric)
    phosphorousamount = Column(Numeric)
    pottasiumamount = Column(Numeric)
    organiccarbonamount = Column(Numeric)
    dateofsowing = Column(DateTime)
    methodofsowing = Column(Integer)
    varietyused = Column(Integer)
    methodofweeding = Column(Integer)
    amountofseed = Column(Integer)
    dateofharvest = Column(DateTime)
    daysleftforharvest = Column(Integer)
    methodofretting = Column(Integer)
    sourceofwater = Column(Integer)
    availabilityofwater = Column(Boolean)
    qualityofwashingwater = Column(Boolean)
    daysrequiredforcompleteretting = Column(String)
    rainfall = Column(Numeric)
    temperature = Column(String)
    humidity = Column(String)
