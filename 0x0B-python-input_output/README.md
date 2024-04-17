# 0x0B Python - Input/Output

This directory contains exercises and examples related to input and output (I/O) operations in Python. The focus is on reading from and writing to files, handling file objects, and utilizing various methods and techniques for input and output operations in Python.

## Learning Objectives

By working through the contents of this directory, you will:

- Understand how to read from and write to files in Python.
- Learn about different file modes and how to use them effectively.
- Explore techniques for handling file objects, such as iterating over lines and seeking.
- Gain familiarity with input/output functions and methods provided by Python, such as `open()`, `read()`, `write()`, and more.
- Practice using Python's JSON module for working with JSON data.

## Files

- **[0-read_file.py](./0-read_file.py)**: Python script that reads a text file (UTF8) and prints its contents to stdout.
- **[1-number_of_lines.py](./1-number_of_lines.py)**: Python script that reads a text file (UTF8) and prints the number of lines it contains to stdout.
- **[2-read_lines.py](./2-read_lines.py)**: Python script that reads `n` lines of a text file (UTF8) and prints them to stdout.
- **[3-write_file.py](./3-write_file.py)**: Python script that writes a string to a text file (UTF8) and returns the number of characters written.
- **[4-append_write.py](./4-append_write.py)**: Python script that appends a string at the end of a text file (UTF8) and returns the number of characters added.
- **[5-to_json_string.py](./5-to_json_string.py)**: Python function that returns the JSON representation of an object (string).
- **[6-from_json_string.py](./6-from_json_string.py)**: Python function that returns an object represented by a JSON string.
- **[7-save_to_json_file.py](./7-save_to_json_file.py)**: Python function that writes an object to a text file (JSON representation).
- **[8-load_from_json_file.py](./8-load_from_json_file.py)**: Python function that creates an object from a JSON file.
- **[9-add_item.py](./9-add_item.py)**: Python script that adds all arguments to a Python list and saves them to a file.
- **[10-class_to_json.py](./10-class_to_json.py)**: Python function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.
- **[11-student.py](./11-student.py)**: Python class `Student` that defines a student by: (based on 10-class_to_json.py)
  - Public instance attributes `first_name`, `last_name`, and `age`.
  - Includes a `to_json()` method that retrieves a dictionary representation of a `Student` instance.
- **[12-student.py](./12-student.py)**: Python class `Student` that defines a student by: (based on 11-student.py)
  - Public instance attributes `first_name`, `last_name`, and `age`.
  - Includes a `to_json()` method that retrieves a dictionary representation of a `Student` instance (same as 11-student.py).
  - Includes a `reload_from_json()` method that replaces all attributes of the `Student` instance using a dictionary representation.
- **[13-student.py](./13-student.py)**: Python class `Student` that defines a
