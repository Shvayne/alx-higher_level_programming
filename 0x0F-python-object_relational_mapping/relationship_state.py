#!/usr/bin/python3
"""this file is the decalaration of a state"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'state'.

    Attributes:
        id (int): The primary key, auto-generated unique integer.
        name (str): The name of the state, a string with a maximum of 128 character
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

