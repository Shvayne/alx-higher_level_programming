#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    where_to_del = []
    for key, val in a_dictionary.items():
        if val == value:
            where_to_del.append(key)
    for key in where_to_del:
        del a_dictionary[key]
    return a_dictionary
