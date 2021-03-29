#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

type_storage = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities', cascade='delete')
    if (type_storage != 'db'):
        state_id = ""
        name = ""
