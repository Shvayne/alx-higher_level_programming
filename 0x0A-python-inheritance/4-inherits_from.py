#!/usr/bin/python3
"""contains a function that Checks if obj is an instance of a class that inherited 
    (directly or indirectly) from the specified class."""

def inherits_from(obj, a_class):
    """ Check if obj is an instance of a class that inherited 
    (directly or indirectly) from the specified class.
    Args:
        obj: object
        a_class: class to compare
    """
    ob_class = type(obj)
    return ob_class != a_class and issubclass (ob_class, a_class)
