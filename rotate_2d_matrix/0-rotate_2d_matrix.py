#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise, in-place.
    """
    n = len(matrix)

    # Étape 1 : transposer la matrice (lignes <-> colonnes)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Étape 2 : inverser chaque ligne
    for row in matrix:
        row.reverse()
