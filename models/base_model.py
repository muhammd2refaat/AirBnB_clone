#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self):
        """
        Constructor
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
