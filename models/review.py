#!/usr/bin/python3
"""
Review class, that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review (models/review.py):
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string

    """
    place_id = ""
    user_id = ""
    text = ""
