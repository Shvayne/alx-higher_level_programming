#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    max_value = 0
    best_key = None

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best_key = key
    if not best_key:
        return None
    return best_key
