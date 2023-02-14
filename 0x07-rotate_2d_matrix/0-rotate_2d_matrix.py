#!/usr/bin/python3
"""
0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates 2d matrix
    """
    mat_len = len(matrix)
    row_len = len(matrix[0])
    new_list = []

    for i in range(mat_len):
        for j in range(row_len - 1, -1, -1):
            new_list.append(matrix[j][i])

    for i in range(mat_len):
        for j in range(row_len):
            matrix[i][j] = new_list.pop(0)
