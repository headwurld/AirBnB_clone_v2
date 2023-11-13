#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class repr states"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    _cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Lists related city objects """
            list_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
