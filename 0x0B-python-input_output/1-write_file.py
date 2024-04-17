#!/usr/bin/python3
"""this module contains a function that writes to files"""
def write_file(filename="", text=""):
    with open(filename, encoding='utf-8', mode='w') as f:
       return (f.write(text))
