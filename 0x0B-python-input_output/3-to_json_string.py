#!/usr/bin/python3
"""this module contains a function that returns a json rep of a string"""
import json
def to_json_string(my_obj):
    """function to convert an object to a JSON representation of itself
    Args:
        obj: object to convert
    """
    return (json.dumps(my_obj))
