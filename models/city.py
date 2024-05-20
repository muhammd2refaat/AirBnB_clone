#!/usr/bin/python3
"""
City class, that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City (models/city.py):

    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string

    """
    state_id = ""
    name = ""
