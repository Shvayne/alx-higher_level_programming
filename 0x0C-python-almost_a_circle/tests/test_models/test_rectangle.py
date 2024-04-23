#!/usr/bin/python3
"""unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle
import io
import sys

class TestRectangle(unittest.TestCase):
    """unit tests for rectangle class"""

    def test_constructor_default(self):
        """Test initialization with default values"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 3)

    def test_constructor_custom(self):
        """test initialization with custom value"""
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 100)

    def test_width_setter(self):
        """test changing initial width"""
        rect = Rectangle(5, 10)
        rect.width = 15
        self.assertEqual(rect.width, 15)

    def test_height_setter(self):
        """test changing initial height"""
        rect = Rectangle(5, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_x_setter(self):
        """test changing initial x"""
        rect = Rectangle(5, 10)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_y_setter(self):
        """test changing initial y"""
        rect = Rectangle(5, 10)
        rect.y = 4
        self.assertEqual(rect.y, 4)

    def test_invalid_width_type(self):
        """testing for an invalid type"""
        with self.assertRaises(TypeError):
            Rectangle("betty", 5)

    def test_invalid_width_value(self):
        """testing for values <= 0"""
        with self.assertRaises(ValueError):
            Rectangle(-5, 3)

    def test_invalid_height_type(self):
        """test for inavlid width type"""
        with self.assertRaises(TypeError):
            Rectangle(5, "betty")

    def test_invalid_height_value(self):
        """testing for invalid width value"""
        with self.assertRaises(ValueError):
            Rectangle(5, -5)

    def test_invalid_x_type(self):
        """test for invalid x type"""
        with self.assertRaises(TypeError):
            Rectangle(5, 5, "betty")

    def test_invalid_x_value(self):
        """test for a negative x value"""
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -5)

    def test_invalid_y_type(self):
        """test for non int y value"""
        with self.assertRaises(TypeError):
            Rectangle(5, 5, 5, "betty")

    def test_invalid_y_value(self):
        """test for negative y value"""
        with self.assertRaises(ValueError):
            Rectangle(5, 5, 5, -5)

    def test_area(self):
        """test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str_representation(self):
        """test the sring representation of a rectangle instance"""
        rect = Rectangle(5, 10, 2, 3, 100)
        expected_str = "[Rectangle] (100) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_str_represntation_default(self):
        """test string representaion with default values"""
        rect = Rectangle(5, 10)
        expected_str = "[Rectangle] (15) 0/0 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def setUp(self):
        """Redirect stdout to capture printed output"""
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        """Restore stdout after each test"""
        sys.stdout = sys.__stdout__

    def test_display(self):
        """Test the display method"""
        rect = Rectangle(3, 2)
        rect.display()
        expected_output = "###\n###\n\n"
        self.assertEqual(self.stdout.getvalue(), expected_output)

    def test_display_with_position(self):
        """Test the display method with position"""
        rect = Rectangle(3, 2, 2, 1)
        rect.display()
        expected_output = "\n  ###\n  ###\n\n"
        self.assertEqual(self.stdout.getvalue(), expected_output)

    def test_update_with_args(self):
        """Test updating attributes with arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_update_with_fewer_args(self):
        """Test updating with fewer arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_with_more_args(self):
        """Test updating with more arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50, 60, 70)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 40)
        self.assertEqual(rect.y, 50)

    def test_update_with_no_args(self):
        """Test updating with no arguments"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update()
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_update_with_kwargs(self):
        """test method with key worded arguments"""
        rect = Rectangle(1, 2, 3, 5, 6)
        rect.update(id=2, width=25, height=35, x=45, y=55)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 25)
        self.assertEqual(rect.height, 35)
        self.assertEqual(rect.x, 45)
        self.assertEqual(rect.y, 55)



if __name__ == '__main__':
    unittest.main()


