from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal, engine

router = APIRouter()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create user
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# # get user 
# @router.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users

# get user by id 
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# update user
@router.post("/users/{user_id}/update/", response_model=schemas.User)
def create_item_for_user(user: schemas.User,
    user_id: int, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db,user=user)

# get songs
@router.get("/songs/", response_model=list[schemas.Song])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

# create songs
@router.post("/songs/{user_id}/create",response_model=schemas.Song)
def create_song(song: schemas.SongBase,user_id: int, db:Session = Depends(get_db)):
    db_song = crud.create_song(db,song=song, user_id=user_id)
    return db_song



######################################################################3
#################TESTING#############################################

# get songs by user /users/{user_id}/songs
# @router.get("/users/{user_id}/songs", response_model=list[schemas.Song])
# def read_items(user_id: int, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items