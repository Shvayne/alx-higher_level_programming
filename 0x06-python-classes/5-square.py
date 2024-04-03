#!/usr/bin/python3
"""defines a square class
"""
class Square:
    """defines a square class for creation of square objects"""
    def __init__(self, size=0):
        """constructor method

        Args:
            size (int): size of square instance
        """
        self.size = size

    @property
    def size(self):
        """getter method for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the size attribute
        Args:
            value (int): value for size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method foe returning the square area
        returns: the area of a square object
        """
        return (self.__size ** 2)
    def my_print(self):
        """method for printing the triange"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
