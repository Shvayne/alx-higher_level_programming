#!/usr/bin/python3
def print_square(size):
    """prints a square with the letter #
    Args:
        size: size of the intended square 
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) == float:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)
