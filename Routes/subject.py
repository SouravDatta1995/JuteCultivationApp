from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Database import schemas
from Database.crud import crud_subject
from Routes.Dependency import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Subject])
def read_subject(db: Session = Depends(get_db)):
    return crud_subject.get_subjects(db)


@router.post("/", response_model=schemas.Subject)
def add_subject(subject: schemas.SubjectBase, db: Session = Depends(get_db)):
    db_subject = crud_subject.get_subjects_by_name(db, subject.name)
    if db_subject:
        raise HTTPException(status_code=400, detail="Subject already registered")
    return crud_subject.add_subjects(db, subject)
