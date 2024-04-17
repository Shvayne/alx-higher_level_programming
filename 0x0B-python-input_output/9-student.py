#!/usr/bin/python3
"""this module contains a student class"""
class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """contructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of the class"""
        return self.__dict__