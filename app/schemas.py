import email
from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from sqlalchemy import true
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True #Optional field -  Default value gets stored
    # rating: Optional[int] = None # Completely optional - No value gets stored

class PostCreate(PostBase):
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = true

class PostResponse(PostBase):
    # title: str
    # content: str
    # published: bool
    
    id: int
    user_id: int
    user: UserResponse

    class Config:
        orm_mode = true

class PostVote(PostBase):
    Post: PostResponse
    votes: int
    class Config:
        orm_mode = true

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id:Optional[str]=None

class Vote (BaseModel):
    post_id: int
    dir: conint(le=1)