from fastapi import FastAPI

from Routes import jute

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jute.router, prefix="/jute", tags=["Jute"], responses={404: {"description": "Not found"}})
