#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squared_row = []
        for x in row:
            squared_row.append(x ** 2)
        new_matrix.append(squared_row)
    return new_matrix
