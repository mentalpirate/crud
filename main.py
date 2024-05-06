from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from routes import router
import models 
from database import SessionLocal, engine
# database migratition
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/user", tags=["Users"])
