#!/usr/bin/python3
"""this module contains a square class"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """this class defines a square object"""
    def __init__(self, size):
        """instantiation method"""
        super().integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        return ("[Square] {}/{}".format(self.__size, self.__size))
