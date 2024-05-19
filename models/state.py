#!/usr/bin/python
""" state class  inheriting from the 'BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class inheriting from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)