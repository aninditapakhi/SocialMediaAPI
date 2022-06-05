from enum import unique
import imp
# from tkinter import CASCADE #Fixing Heroku deploy issue
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, false, true
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, nullable = False)
    title = Column (String, nullable = False)
    content = Column (String, nullable = False)
    published = Column (Boolean, server_default = 'TRUE', nullable = False)
    created_at = Column (TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
    user_id = Column (Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable= False)

    user = relationship("User")

class User(Base):
    __tablename__="users"
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    id = Column(Integer, primary_key = True, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key = True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key = True)
    