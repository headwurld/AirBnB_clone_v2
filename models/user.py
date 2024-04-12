#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    places = relationship(
        "Place",
        backref='user',
        cascade="all, delete-orphan",
        passive_deletes=True)

    reviews = relationship(
        "Review", 
        backref="user", 
        cascade="all, delete",
        passive_deletes=True)

    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)
