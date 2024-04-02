#!/usr/bin/python3
import sys

'''
a function that prints an integer
'''
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except ValueError as e:
        sys.stderr.write("Exception: " + str(e))
        return False

