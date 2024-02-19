#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import type_of_storage


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        """ if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        if "updated_at" not in kwargs:
            self.updated_at = datetime.now() """

        # Set default value
        """ kwargs.setdefault('updated_at', datetime.now())
        kwargs.setdefault('created_at', datetime.now()) """

        """ if isinstance(kwargs['updated_at'], str):
            kwargs['updated_at'] = datetime.strptime(
                            kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
        if isinstance(kwargs['created_at'], str):
            kwargs['created_at'] = datetime.strptime(
                            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        ) """

        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            # self.__dict__.update(kwargs)

            # Assign additional attributes from kwargs to instance
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""

        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__

        for key in dictionary:
            if isinstance(dictionary[key], datetime):
                dictionary[key] = dictionary[key].isoformat()

        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        ''' deletes the object '''

        from models import storage

        storage.delete(self)
