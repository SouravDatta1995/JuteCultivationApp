from sqlalchemy.orm import Session

from Database import models, schemas


def get_subjects(db: Session):
    return db.query(models.Subject).all()


def get_subjects_by_name(db: Session, subject_name: str):
    return db.query(models.Subject).filter(models.Subject.name == subject_name).first()


def add_subjects(db: Session, subject: schemas.SubjectBase):
    db_subject = models.Subject(name=subject.name)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject
