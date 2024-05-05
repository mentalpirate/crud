from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for user creation and management 
class UserBase(BaseModel):
    full_name: str
    profile: Optional[str] = None
    email: str
    google_id: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

# Schema for song management 
class SongBase(BaseModel):
    song_name: str
    song_url: str
    cover_image_url: Optional[str]
    created_at: datetime
    play_count: int
    likes_count: int
    user_id: int

class SongCreate(SongBase):
    pass

class Song(SongBase):
    song_id: int

    class Config:
        orm_mode = True

# Schema for likes 
class LikesBase(BaseModel):
    song_id: int
    user_id: int
    created_at: datetime

class LikesCreate(LikesBase):
    pass

class Likes(LikesBase):
    like_id: int

    class Config:
        orm_mode = True
