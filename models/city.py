#!/usr/bin/python
"""  city class  inheriting from the 'BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """City class  inheriting from the 'BaseModel """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization """
        super().__init__(*args, **kwargs)