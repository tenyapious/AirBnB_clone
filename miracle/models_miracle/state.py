#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Call for a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
