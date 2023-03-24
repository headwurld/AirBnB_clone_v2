#!/usr/bin/python3
"""Defines the Place class."""
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv
import models


# Define a many-to-many relationship table for places and amenities
if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity_table = Table("place_amenity", Base.metadata,
                                Column("place_id", String(60),
                                       ForeignKey("places.id"),
                                       primary_key=True, nullable=False),
                                Column("amenity_id", String(60),
                                       ForeignKey("amenities.id"),
                                       primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Represents a place to stay in the system."""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenities = relationship(
        "Amenity", secondary="place_amenity", viewonly=False,
        overlaps="place_amenities")
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """Returns the list of reviews associated with this place."""
            reviews_list = []
            for review in storage.all("Review").values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Returns the list of amenities associated with this place."""
            amenities = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            """Sets the list of amenities associated with this place."""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
