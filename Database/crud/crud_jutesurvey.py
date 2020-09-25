from sqlalchemy.orm import Session

from Database import models, schemas


def getSurveyInput_by_name(db: Session, name: str):
    return db.query(models.JuteSurveyInputs).filter(models.JuteSurveyInputs.name == name).all()


def addSurveyInput(db: Session, survey_details: schemas.JuteSurveyInputBase):
    db_surveyinput = models.JuteSurveyInputs(**survey_details.dict())
    db.add(db_surveyinput)
    db.commit()
    db.refresh(db_surveyinput)
    return db_surveyinput
