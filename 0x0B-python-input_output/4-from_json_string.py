#!/usr/bin/python3
"""this module contains a function that returns a obj rep of json str"""
import json
def from_json_string(my_str):
    """
    a function to deserialize
    Args:
        my_str: string to deserialize
    """
    return (json.loads(my_str))
