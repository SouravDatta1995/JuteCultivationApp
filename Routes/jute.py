from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Database import schemas
from Database.crud import crud_jutesurvey
from Routes.Dependency import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.JuteSurveyInput])
def read_survey_by_name(name: str, db: Session = Depends(get_db)):
    return crud_jutesurvey.getSurveyInput_by_name(db, name)


@router.post("/", response_model=schemas.JuteSurveyInput)
def add_survey_input(jutesurveyinput: schemas.JuteSurveyInputBase, db: Session = Depends(get_db)):
    # db_subject = crud_jutesurvey.(db, subject.name)
    # if db_subject:
    #     raise HTTPException(status_code=400, detail="Subject already registered")
    return crud_jutesurvey.addSurveyInput(db, jutesurveyinput)
