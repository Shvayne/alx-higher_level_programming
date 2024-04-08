#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements in a matrix(list of lists)
    Args:
        matrix: the list of lists we will be dividing
        div: the denominator
    Return: A new matrix with the new values
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of list) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of list) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of list) of integers/floats")
    length = all(len(row) == len(matrix[0]) for row in matrix)
    if not length:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for row in matrix:
        small_list = []
        for num in row:
            small_list.append(round(num / div, 2))
        new_list.append(small_list)
    return new_list
