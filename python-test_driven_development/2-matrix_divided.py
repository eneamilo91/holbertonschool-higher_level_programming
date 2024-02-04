#!/usr/bin/python3

"""Module that divides the elements of a matrix"""


def matrix_divided(matrix, div):
    """Func that performs the division"""
    new_matrix = []
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, int) and not isinstance(div, float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(row)
