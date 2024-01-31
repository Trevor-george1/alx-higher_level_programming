#!/usr/bin/python3
"""
function tha divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    # check if matrix is alist of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    #check if each row is of same size
    if any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of matrix must have same size")
    
    #divide each element by div and round of 2 decimal places
    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
