from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from Database import schemas
from Database.crud import crud_user
from Routes.Dependency import get_db

router = APIRouter()


@router.get("/{name}", response_model=schemas.User)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud_user.add_user(db, user)
