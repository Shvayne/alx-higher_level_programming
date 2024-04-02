#!/usr/bin/python3

'''
A function that divides 2 integers and prints the result.
'''
def safe_print_division(a, b):
    try:
        if not isinstance(a + b, int):
            raise TypeError
        if (a == 0 or b == 0):
            raise ZeroDivisionError
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        if result is not None:

            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
    return result
