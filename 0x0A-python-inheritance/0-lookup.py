#!/usr/bin/python3
"""this module contains a function lookup that returns the list of available mrthods of an object"""
def lookup(obj):
    """function to return the list of available methods"""
    return list(dir(obj))
