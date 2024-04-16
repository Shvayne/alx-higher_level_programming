#!/usr/bin/python3
"""this module contains a Myint class that inhert from int"""
class MyInt(int):
    """an int subclass"""
    def __eq__(self, other):
        """override the == operator"""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """override the != operator"""
        return super().__eq__(other)
