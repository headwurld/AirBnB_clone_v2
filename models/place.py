#!/usr/bin/python3
"""Place Module for HBNB project"""
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import type_of_storage
from models.review import Review
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"

    if type_of_storage == 'db':
        reviews = relationship(
            'Review',
            cascade='all, delete-orphan',
            backref='place'
            )
    else:
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []

        @property
        def reviews(self):
            """
            Returns the list of Review instances with place_id
            equal to the current Place.id. It's the FileStorage
            relationship between Place and Review.

            """

            from models import storage

            all_reviews = storage.all(Review)
            reviews = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
