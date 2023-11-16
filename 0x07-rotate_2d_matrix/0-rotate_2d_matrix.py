#!/usr/bin/python3
"""_summary_
"""


def transpose_matrix(matrix, n):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    n = len(matrix)

    transpose_matrix(matrix, n)

    reverse_matrix(matrix)

    return matrix
