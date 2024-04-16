#!/usr/bin/python3
"""modlue that contains a function that can check if an attribute can be added"""

def add_attribute(obj, attr, value):
    """checks if its possible to add an attribute to an obj and adds it"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
