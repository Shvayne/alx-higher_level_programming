#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """defines a square by a private size attribute.
    """
    def __init__(self, size):
        """constructor method

        Args:
            size: size of square instance
        """
        self.__size = size