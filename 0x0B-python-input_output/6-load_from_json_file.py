#!/usr/bin/python3
"""this module contains a function that creates an object from a json file"""
import json
def load_from_json_file(filename):
    """function to deserialize a file
    Args:
        filename: the file holdin the data
    Returns: the deserialized obj
    """
    with open(filename, encoding='utf-8', mode='r') as file:
        return json.load(file)
    