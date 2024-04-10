#!/usr/bin/python3
class Rectangle():
    def __init__(self, width=0, height=0):
        """constructor method
        Args:
            width (int, optional): width of the rectangle
            height(int, optional):height of the rectangle
        """
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
    
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """getter method for width attr"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter method for width attr
        Args:
            value (int): value to set width to
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """getter method for height attr"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter method for height attr
        Args:
            value (int): value to set height to
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
