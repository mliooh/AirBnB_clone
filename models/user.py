#!/usr/bin/python

""" User class  inheriting from the BaseModel ."""

from models.base_model import BaseModel


class User(BaseModel):
    """ initialization  from  the BaseModel. """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)