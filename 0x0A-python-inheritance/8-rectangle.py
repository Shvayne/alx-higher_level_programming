#!/usr/bin/python3
"""this module contains a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """a subclass of a geometry class"""
    def __init__(self, width, height):
        """instantiation method"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
