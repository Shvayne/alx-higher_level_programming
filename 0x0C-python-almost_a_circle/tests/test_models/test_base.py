#!/usr/bin/python3
"""Tests cases for base class"""
import unittest
from models.base import Base
from models.square import Square
import json

class TestBaseClass(unittest.TestCase):
    """Test cases for Base class"""

    def test_id_none(self):
        """test no id"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """Test initialization of base object with Id provided"""
        b = Base(10)
        self.assertEqual(10, b.id)

    def test_id_zero(self):
        """test sendig a zero id"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """test with a negative id"""
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        """test a non int id"""
        b = Base("sza")
        self.assertEqual("sza", b.id)

    def test_id_list(self):
        """test a non int id"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        """test an id that is not an int"""
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        """test an id that is not an int """
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        """Testing the json string"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        """test the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_empty(self):
        """test the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


if __name__ == "__main__":
    unittest.main()

