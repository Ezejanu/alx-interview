#!/usr/bin/python3
"""Rotate 2d Matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D square matrix 90 degrees clockwise in-place.

    Args:
    matrix (list of list): The 2D square matrix to be rotated.

    Returns:
    None: The matrix is modified in-place. No value is returned.
    """

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
