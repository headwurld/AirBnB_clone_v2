#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Instatiates a new model """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            try:
                kwargs['updated_at'] = datetime\
                    .strptime(kwargs['updated_at'],
                              '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.\
                    strptime(kwargs['created_at'],
                             '%Y-%m-%dT%H:%M:%S.%f')
            except Exception as e:
                print("Error parsing dates: ", kwargs)

            # Ensure that 'id' is present in kwargs or generate a new one
            kwargs['id'] = kwargs.get('id', str(uuid.uuid4()))

            if '__class__' in kwargs:
                del kwargs['__class__']

            # Iterate over kwargs and set instance attributes
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)

            self.__dict__.update(kwargs)

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
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        # dictionary.pop('_sa_instance_state', None)

        # Remove _sa_instance_state if it exists
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        """
        Ensure that 'created_at' and 'updated_at'
        are datetime objects before calling isoformat
        """
        if isinstance(dictionary['created_at'], datetime):
            dictionary['created_at'] = dictionary['created_at'].isoformat()

        if isinstance(dictionary['updated_at'], datetime):
            dictionary['updated_at'] = dictionary['updated_at'].isoformat()

        # dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """ Deletes the current instance from the storage. """
        from models import storage
        storage.delete(self)
