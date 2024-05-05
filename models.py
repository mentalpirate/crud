from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer,primary_key=True)
    full_name = Column(String, unique=True)
    profile = Column(String)
    email = Column(String, unique=True, index=True)
    google_id = Column(String)
    class Config:
        orm_mode = True

class Song(Base):
    __tablename__ = "songs"
    song_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("users.user_id"))
    song_name = Column(String)
    song_url = Column(String)
    cover_image_url = Column(String)
    created_at = Column(DateTime)
    play_count = Column(Integer)
    likes_count = Column(Integer)
    class Config:
        orm_mode = True

class Likes(Base):
    __tablename__ = "likes"
    like_id = Column(Integer, primary_key=True, unique=True)
    song_id = Column(Integer, ForeignKey("songs.song_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime)
    class Config:
        orm_mode = True
        