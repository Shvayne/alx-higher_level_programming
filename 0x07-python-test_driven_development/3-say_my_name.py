#!/usr/bin/python3
import sys
def say_my_name(first_name, last_name=""):
    """introduces itself
    Args:
        first_name: first input string
        last_name: second input string, empty string by default
    """
    # if len(sys.argv) <= 1:
    #     raise ValueError("greet(), expects at least 1 argument")
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")
    
    print("My name is {:s} {:s}".format(first_name, last_name))
  