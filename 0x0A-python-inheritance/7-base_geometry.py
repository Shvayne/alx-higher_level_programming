#!/usr/bin/python3
"""this module contains a shape class"""
class BaseGeometry:
    """a shape class"""
    def area(self):
        """returns area of the shape"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates a value
        Args:
            name: always a string
            value: a value associated with a name
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
