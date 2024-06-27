#!/usr/bin/python3
"""This file contains the class definition of City"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    City class that links to the MySQL table 'state'.
    Attributes:
        id (int): The primary key, auto generated
        state_id (int): the secondary key from states.id
        name(str): the name of the city, maximum of 128
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

