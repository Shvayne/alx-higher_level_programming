# 0x0A-python-inheritance

## Overview
This repository contains Python code examples and explanations related to inheritance in Python. Inheritance is a fundamental concept in object-oriented programming (OOP) that allows classes to inherit attributes and methods from other classes.

## Contents
The repository includes the following files and directories:

- `0-lookup.py`: Python script that defines a function `lookup(obj)` which returns the list of available attributes and methods of an object.
- `1-my_list.py`: Python script that defines a class `MyList` which inherits from the built-in class `list`.
- `2-is_same_class.py`: Python script that defines a function `is_same_class(obj, a_class)` which checks if an object is an instance of a given class.
- `3-is_kind_of_class.py`: Python script that defines a function `is_kind_of_class(obj, a_class)` which checks if an object is an instance of a class or a subclass.
- `4-inherits_from.py`: Python script that defines a function `inherits_from(obj, a_class)` which checks if an object inherits from a class (but not the same class).
- `5-base_geometry.py`: Python script that defines an empty class `BaseGeometry`.
- `6-base_geometry.py`: Python script that defines a class `BaseGeometry` with a method `def area(self):` that raises an Exception with the message `area() is not implemented`.
- `7-base_geometry.py`: Python script that defines a class `BaseGeometry` with methods `def area(self):` and `def integer_validator(self, name, value):`.
- `8-rectangle.py`: Python script that defines a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
- `9-rectangle.py`: Python script that defines a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
- `10-square.py`: Python script that defines a class `Square` that inherits from `Rectangle` (`9-rectangle.py`).

## Usage
You can run each Python script individually to see the examples in action. For example:
```bash
python 0-lookup.py
```