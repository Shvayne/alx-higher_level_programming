#!/usr/bin/python3

def max_integer(my_list=[]):
    max_value = my_list[0]
    if not my_list:
        return None
    for digit in my_list:
        if digit > max_value:
            max_value = digit
    return max_value
