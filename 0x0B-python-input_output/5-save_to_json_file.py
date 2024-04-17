#!/usr/bin/python3
"""this module contains a function that writes an object to a text file using a JSON representation"""
import json
def save_to_json_file(my_obj, filename):
    """function to write an object to a text file using a JSON representation
    Args:
        my_obj: object to serialize
        filename: file to write to
    """
    with open(filename, encoding='utf-8', mode='a') as file:
        json.dump(my_obj, file)
        file.write('\n')
