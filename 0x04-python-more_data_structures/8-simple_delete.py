#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        pass
    del a_dictionary[key]
    return a_dictionary
