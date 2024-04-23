#!/usr/bin/python3
"""Tests cases for base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_default_initialization(self):
        """test default initialzation of base object"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_initialization(self):
        """Test initialization of base object with Id provided"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_uniqueness_of_ids(self):
        """Test uniqueness of IDs among Base objects"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b2.id, b3.id)

    def test_negative_int_initialization(self):
        """Test negative ID initialization"""
        b = Base(-1)
        self.assertEqual(b.id, -1)

    def test_initialization_with_non_int_id(self):
        """test string initialization"""
        b = Base("maria")
        self.assertEqual(b.id, "maria")

    def test_initialization_with_list(self):
        """test for list initialization"""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_zero(self):
        """test for zero id initialzation"""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_tuple(self):
        """Test for tuple id initialization"""
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))

if __name__ == '__main__':
    unittest.main()

