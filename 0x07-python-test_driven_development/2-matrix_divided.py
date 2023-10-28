#!/usr/bin/python3
"""Module of "2-matrix_divided"."""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            # Check if the element is an integer or float
            if not isinstance(i, (int, float)):
                raise TypeError(message)
            else:
                new_row.append(round(i / div, 2))
        new_matrix.append(new_row)

    return new_matrix
