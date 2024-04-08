#!/usr/bin/python3
"""A function to add two integers"""

def add_integer(a, b=98):
    """Adds two integers together
    Args:
        a: first int
        b: second int
    Returns:
        sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return (int(a) + int(b))
