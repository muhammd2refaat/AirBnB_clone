#!/usr/bin/python3
"""Defines the User class that inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""