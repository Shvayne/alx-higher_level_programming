#!/usr/bin/python3
"""defines a square class
"""
class Square:
    """defines a square class for creation of square objects"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor method

        Args:
            size (int): size of square instance
            position (tuple):
            position of rectangle
        """
        self.size = size
        self.position = position

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
    @property
    def position(self):
        """getter method for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):

        """setter method  for attribute
        Args:
            value(tuple): new value for position attribue
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
             raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


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
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
