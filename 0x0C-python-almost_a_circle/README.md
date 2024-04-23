# 0x0C Python Almost a Circle

This project is part of the ALX software engineering curriculum and is focused on practicing object-oriented programming (OOP) concepts in Python. The project involves creating classes and implementing inheritance, encapsulation, and polymorphism to model basic geometric shapes, particularly rectangles and squares, and to apply various operations on them.

## Project Structure

The project consists of the following files and directories:

- **tests/**: This directory contains all the unit tests for the project to ensure its functionality.
- **models/**: This directory contains Python modules implementing the classes and methods required for modeling rectangles and squares.
- **README.md**: This file provides an overview of the project and instructions for usage.

## Classes

1. **Base**: The `Base` class serves as the base class for all other classes in the project. It provides a simple implementation of a unique identifier for each instance.
2. **Rectangle**: The `Rectangle` class represents a rectangle object and inherits from the `Base` class. It implements methods for calculating area, perimeter, and string representation of the rectangle.
3. **Square**: The `Square` class represents a square object and inherits from the `Rectangle` class. It overrides methods from the `Rectangle` class to accommodate square-specific behavior.

## Usage

To use this project, follow these steps:

1. Clone the repository:

git clone https://github.com/your_username/0x0C-python-almost_a_circle.git


2. Navigate to the project directory:

cd 0x0C-python-almost_a_circle


3. You can use the classes provided in the `models/` directory in your Python scripts as follows:

```python
from models.rectangle import Rectangle
from models.square import Square

# Example usage of Rectangle class
r1 = Rectangle(10, 5)
print(r1.area())
print(r1.perimeter())
print(r1)

# Example usage of Square class
s1 = Square(5)
print(s1.area())
print(s1.perimeter())
print(s1)

```
4. To run the unit tests, navigate to the tests/ directory and execute the test script:
cd tests
python test_models.py
