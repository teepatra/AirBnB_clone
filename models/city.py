#!/usr/bin/env python3
""" class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits BaseModel
        Public class attribute
            state_id: (str) - State.id
            name: (str) - City name
    """
    state_id = ""
    name = ""
