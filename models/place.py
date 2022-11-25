#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os
from os import getenv
from models.review import Review
from models.amenity import Amenity


Table('place_amenity', Base.metadata,
      Column('place_id', String(60), ForeignKey("places.id"),
             primary_key=True, nullable=False),
      Column('amenity_id', String(60), ForeignKey("amenities.id"),
             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    name = Column(String(128), nullable=False)

    description = Column(String(1024), nullable=True)

    number_rooms = Column(Integer, nullable=False, default=0)

    number_bathrooms = Column(Integer, nullable=False, default=0)

    max_guest = Column(Integer, nullable=False, default=0)

    price_by_night = Column(Integer, nullable=False, default=0)

    latitude = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)

    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary='place_amenity',
                             back_populates="place_amenities", viewonly=False)

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """getter for FileStorage"""
            reviews = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """getter for FileStorage"""
            amenities = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """setter for FileStorage"""
            if type(obj) == Amenity:
                self.amenities_ids.append(obj.id)
