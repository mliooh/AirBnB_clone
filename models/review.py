#!/usr/bin/python
"""review class  inheriting from the 'BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class  inheriting from the 'BaseModel."""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)