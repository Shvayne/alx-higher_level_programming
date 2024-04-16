#!/usr/bin/python3
"""this module contains a shape class"""
class BaseGeometry:
    """a shape class"""
    def area(self):
        """returns area of the shape"""
        raise Exception("area() is not implemented")
