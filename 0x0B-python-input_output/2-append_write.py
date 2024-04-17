#!/usr/bin/python3
"""this module contains a function that appends to a file"""
def append_write(filename="", text=""):
    """this function appends to a file
    Args:
        filename: name of the file
        text: text to be appended
    """
    with open(filename, encoding='utf-8', mode='a') as f:
        return (f.write(text))
