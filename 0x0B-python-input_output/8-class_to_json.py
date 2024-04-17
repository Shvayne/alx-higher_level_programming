#!/usr/bin/python3
"""this module contains a function that serializes data"""
import json
def class_to_json(obj):
    """this function returns the dictionary description witn simple data structures and recursivelyh handles more complex ones"""
    return (obj.__dict__)