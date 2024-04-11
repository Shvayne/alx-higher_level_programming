#!/usr/bin/python3
"""this module contains a rectangle class"""
class Rectangle():
    """defines a rectangle object"""
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """constructor method
        Args:
            width (int, optional): width of the rectangle
            height(int, optional):height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
    
    def __str__(self):
        """prints the string reprentation of the rectangle"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + '\n'
        return rectangle.rstrip()
    
    def __repr__(self):
        """returns the string represenation of a rectangle class that can be used to create new instances"""
        return f"Rectangle({self.__width}, {self.__height})"
    def __del__(self):
        """cleanup method for deleting a rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
