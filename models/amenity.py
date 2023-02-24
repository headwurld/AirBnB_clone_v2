#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ The Amenity class, contains name """
    if models.storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
