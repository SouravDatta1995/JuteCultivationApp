from sqlalchemy.orm import Session

from Database import models, schemas


def get_user(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.name == user_name).first()


def add_user(db: Session, user: schemas.UserBase):
    db_user = models.User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
