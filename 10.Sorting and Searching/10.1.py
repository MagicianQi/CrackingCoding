# -*- coding: utf-8 -*-

"""
Question 10.1:
    Sorted Merge：You are given two sorted arrays, A and B, where A has a large enough buffer at end to hold B.
                  Write a method to merge B into A in sorted order.
"""


def merge(A, B, A_len, B_len):
    """
    Take O(m+n) time and O(1) space
    :param A: List A
    :param B: List B
    :param A_len: Length Of A
    :param B_len: Length Of B
    :return:
    """
    index = A_len + B_len - 1
    A_index = A_len - 1
    B_index = B_len - 1
    while B_index >= 0:
        if index >= 0 and A[A_index] > B[B_index] and A_index >= 0:
            A[index] = A[A_index]
            A_index -= 1
        else:
            A[index] = B[B_index]
            B_index -= 1
        index -= 1
    return A


if __name__ == '__main__':
    A = [1, 4, 6, 9, 23, None, None, None, None, None]
    B = [2, 5, 10, 11, 30]
    print('A: ', end='')
    print(A)
    print('B: ', end='')
    print(B)
    merge_list = merge(A, B, 5, 5)
    print('Merge: ', end='')
    print(merge_list)
