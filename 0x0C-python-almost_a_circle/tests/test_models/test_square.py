#!/usr/bin/python3
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""Run test cases for square module"""

class test_square(unittest.TestCase):
    """test square"""
    def setUp(self):
        """initializing instance with width and height params
        """
        self.s = Square(3)

    def tearDown(self):
        """delete created instance"""
        try:
            os.remove("Square.json")
        except:
            pass
        del self.s

    def test_width(self):
        """test width getter"""
        self.assertEqual(self.s.width, 3)
    
    def test_width_string(self):
        """test initialization with string"""
        with self.assertRaises(TypeError):
            square = Square("betty")

    def test_width_bool(self):
        """test initialization with boolean"""
        with self.assertRaises(TypeError):
            sqaure = Square(True)

    def test_width_list(self):
        """test initialization with list"""
        with self.assertRaises(TypeError):
            sqaure = Square([20, 40])
    
    def test_width_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            square = Square(-4)


    def test_height(self):
        """testin the height getter"""
        self.assertEqual(self.s.height, 3)

    def test_x(self):
        """test for the square x getter and setter"""
        self.s.x = 54
        self.assertEqual(self.s.x, 54)
        self.assertEqual(self.s.y, 0)
    
    def test_x_string(self):
        """Testing x with string"""
        with self.assertRaises(TypeError):
            square = Square(1, "46")

    def test_x_bool(self):
        """Test x for boolean value initialization"""
        with self.assertRaises(TypeError):
            square = Square(1, True)

    def test_x_list(self):
        """Test x with list initiliztion value"""
        with self.assertRaises(TypeError):
            square = Square(1, [10, 6])
    
    def test_x_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            square = Square(4, -3)


    def test_y(self):
        """test the y getter and setter methods"""
        self.s.y = 45
        self.assertEqual(self.s.y, 45)
        self.assertEqual(self.s.x, 0)

    def test_y_string(self):
        """Testing for string initialization"""
        with self.assertRaises(TypeError):
            square = Square(1, 7, "46")

    def test_y_bool(self):
        """Testing for boolean init"""
        with self.assertRaises(TypeError):
            square = Square(1, 7, True)

    def test_y_list(self):
        """Testing y list initialization"""
        with self.assertRaises(TypeError):
            square = Square(1, 7, [10, 6])

    def test_id(self):
        """test the id of the square"""
        square = Square(2, 0, 0, 199)
        self.assertEqual(square.id, 199)

    def test_y_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            square = Square(4, 2, -3)

    def test_str_overload(self):
        square = Square(5, 8, 7, 88)
        self.assertEqual(square.__str__(), "[Square] (88) 8/7 - 5")

    def test_update_id(self):
        """tests for the update method"""
        self.s.update(54)
        self.assertEqual(self.s.id, 54)

    def test_update_width(self):
        """Tests for the update method"""
        self.s.update(54, 30)
        self.assertEqual(self.s.width, 30)

    def test_update_height(self):
        """Tests for the update method"""
        self.s.update(54, 10)
        self.assertEqual(self.s.height, 10)

    def test_update_x(self):
        """Tests for the update method"""
        self.s.update(54, 30, 10)
        self.assertEqual(self.s.x, 10)

    def test_update_y(self):
        """Tests for the update method"""
        self.s.update(54, 30, 6, 2)
        self.assertEqual(self.s.y, 2)

    def test_to_dictionary(self):
        """test the to_dictionary method"""
        square = self.s.to_dictionary()
        expected = {'id': self.s.id, 'size': self.s.size, 'x': self.s.size, 'y': self.s.y}
        self.assertEqual(square, expected)

    
    

    
