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

    def __str__(self):
        """prints details about the class in a redable format"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
    
    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)
