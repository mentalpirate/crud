from sqlalchemy.orm import Session

import models 
import schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email,full_name=user.full_name, profile=user.profile,google_id = user.google_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_song(db: Session, song: schemas.SongCreate, user_id: int):
    db_song = models.Song(song_name=song.song_name,song_url=song.song_url,play_count=song.play_count,created_at=song.created_at, likes_count = song.likes_count, user_id=user_id)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()




def create_user_item(db: Session, user: schemas.User,email: str,full_name: str, profile: str,google_id: str):
    _user =  get_user(db=db, user_id=user.user_id)
    _user.full_name = full_name
    _user.profile = profile
    _user.email = email
    _user.google_id = google_id
    
    db.commit()
    db.refresh(_user)
    return _user
