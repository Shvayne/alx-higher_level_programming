#!/usr/bin/python3
"""this module contains a student class"""
class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """contructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of the class"""
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
                return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
