# -*- coding: utf-8 -*-

"""
Question 1.7:
    Rotate Matrix : Given an image represented by an N*N matrix, where each pixel in the image is 4 bytes,
                    write a method to rotate the image by 90 degrees.Can you do this in place?
"""

import numpy as np


def rotateMatrix(matrix):
    """
    Take O(n2) time and O(1) space
    tips: 1.list/mat[a:b:c] a: start b: end c: step
          2.*[[1], [2]] = [1], [2] | * = get list value
    :param matrix: input matrix
    :return: output matrix
    """
    matrix[:] = map(list, zip(*matrix[::-1]))
    return np.mat(matrix)


if __name__ == '__main__':
    matrix = np.random.randint(0, 10, [5, 5])
    print(matrix)
    print((rotateMatrix(matrix.tolist())))
