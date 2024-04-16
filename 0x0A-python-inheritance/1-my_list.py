#!/usr/bin/python3
"""this module contains a subclass MyList of a parent List class"""
class MyList(list):
    """subclass Mylist inheriting from list class"""
    def print_sorted(self):
        """prints the elements of the list in ascending order"""
        print(sorted(self))
