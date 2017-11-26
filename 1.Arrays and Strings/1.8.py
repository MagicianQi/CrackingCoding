# -*- coding: utf-8 -*-

"""
Question 1.8:
    Zero Matrix: Write an algorithm such that if an element in an M*N matrix is 0, its entire row and
                 column are set to 0.
"""

import numpy as np


def zeroMatrix(matrix):
    """
    Take O(n2) time and O(1) space
    :param matrix: Input Matrix
    :return: Output Matrix
    """
    indexes = {'row': [], 'col': []}
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 0:
                if i not in indexes['row']:
                    indexes['row'].append(i)
                if j not in indexes['col']:
                    indexes['col'].append(j)
    for i in range(matrix.shape[0]):
        if i in indexes['row']:
            for j in range(matrix.shape[1]):
                matrix[i, j] = 0
    for j in range(matrix.shape[1]):
        if j in indexes['col']:
            for i in range(matrix.shape[0]):
                matrix[i, j] = 0


if __name__ == '__main__':
    matrix = np.random.randint(0, 10, [5, 5])
    print(matrix)
    zeroMatrix(matrix)
    print(matrix)
