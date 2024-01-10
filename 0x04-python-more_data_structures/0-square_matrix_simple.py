#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        result_row = []
        for i in row:
            squared_number = i ** 2
            result_row.append(squared_number)
        result_matrix.append(result_row)
    return result_matrix
