#!/usr/bin/python3
"""Module containing function to check if an object is an instance of a class"""
def is_same_class(obj, a_class):
    """checks if an obj is an instance of a class"""
    return type(obj) is a_class
