#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='State', cascade='delete')
    else:
        name =""

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """getter method"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list