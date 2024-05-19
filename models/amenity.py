#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class  containing Amenities."""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)