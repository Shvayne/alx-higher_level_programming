#!/usr/bin/python3
"""unittests for max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    """unit tests for max_integer"""

    def test_ordered(self):
        """test an ordered list of integers"""
        ordered_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered_list), 5)

    def test_unordered(self):
        """test an unordered list of integers"""
        unordered_list = [4, 5, 2, 1, 6]
        self.assertEqual(max_integer(unordered_list), 6)

    def test_max_at_begginning(self):
        """test a list with a starting max value."""
        max_at_beginning = [6, 4, 5, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 6)

    def test_max_at_end(self):
        """test a list with an ending max value"""
        max_at_ending = [1, 4, 5, 6, 9]
        self.assertEqual(max_integer(max_at_ending), 9)
    
    def test_single(self):
        """test a list of one int"""
        single_list = [10]
        self.assertEqual(max_integer(single_list), 10)

    def test_empty_list(self):
        """test an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_float(self):
        """test a mixed list of flots and integers"""
        float_list = [1.1, 3.4, 5.6, 5, 6, 7, 9.0, 9.3]
        self.assertEqual(max_integer(float_list), 9.3)

    def test_empty_string(self):
        """test an empty string"""
        empty_string = ""
        self.assertEqual(max_integer(empty_string), None)

    if __name__ == '__main__':
        unittest.main()
    
    