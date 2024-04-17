#!/usr/bin/python3
"""this module contains a function that reads a textfile"""
def read_file(filename=""):
    """a function that reads a file"""
    with open(filename, encoding='utf-8', mode='r') as f:
        for line in f:
            print(line, end='')
