from fastapi import FastAPI

from Routes import user, subject

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}})
app.include_router(subject.router, prefix="/subjects", tags=["Subjects"], responses={404: {"description": "Not found"}})
