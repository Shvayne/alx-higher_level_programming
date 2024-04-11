#!/usr/bin/python3
"""module that conatains a square class"""

class Square:
    """defines a square class for creation of square objects"""
    def __init__(self, size=0):
        """constructor method

        Args:
            size (int): size of square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

