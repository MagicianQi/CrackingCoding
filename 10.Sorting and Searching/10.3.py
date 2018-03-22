# -*- coding: utf-8 -*-

"""
Question 10.3:
    Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown number of
                             times, write code to find an element in the array. You may assume that the array
                             was originally sorted in increasing order.
    EXAMPLE
        Input: find in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
        Output: 8(the index of 5 in the array)
"""


def rotate_search(int_list, num):
    """
    Take O(logn) time and O(1) space
    :param int_list: Rotated Array
    :param num: Number To Find
    :return: Number Index
    """
    length = len(int_list)
    left = 0
    right = length - 1
    while left <= right:
        mid = int((left + right) / 2)
        if int_list[mid] == num:
            return mid
        if int_list[mid] < num:
            if int_list[right] >= num:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if int_list[left] <= num:
                right = mid - 1
            else:
                left = mid + 1


if __name__ == '__main__':
    int_list = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    index = rotate_search(int_list, 5)
    print(index)
