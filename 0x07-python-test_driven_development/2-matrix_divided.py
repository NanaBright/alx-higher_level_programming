#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ Check if matrix is a list of lists of integers or floats """
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """ Check if each row of the matrix has the same size """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """ Check if div is a number """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """ Check if div is not equal to zero """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ Perform the division and rounding """
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    """ Return the new matrix """
    return new_matrix
