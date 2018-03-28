# -*- coding: utf-8 -*-

"""
Question 10.4:
    Sorted Search No Size: You are given an array-like data structure Listy which lacks a size method. It does,
                           however, have an elementAt(i) method that returns the element at index i in O(1) time.
                           If i is beyond the bounds of the the data structure, it returns -1.(For this reason, the
                           data structure only supports positive integers) Given a Listy which contains sorted,
                           positive integers, find the index at which an element X occurs. If x occurs multiple times,
                           you may return any index.
"""


class Listy:
    def __init__(self, input_array):
        self.array = input_array

    def elementAt(self, i):
        if i >= len(self.array):
            return -1
        else:
            return self.array[i]


def get_Listy():
    arr = [1, 2, 5, 7, 11, 14, 17, 20, 45, 79, 82, 101, 156]
    list_nosize = Listy(arr)
    return list_nosize


def search(list_nosize, x):
    """
    Take O(logn) time and O(1) space
    :param list_nosize: List No Size
    :param x: Input x
    :return: Index Of x
    """
    index = 1
    while list_nosize.elementAt(index) < x and list_nosize.elementAt(index) != -1:
        index *= 2
    return binary_search(list_nosize, x, index / 2, index)


def binary_search(list_nosize, x, low, high):
    """
    Take O(logn) time and O(1) space
    :param list_nosize: List No Size
    :param x: Input x
    :param low: Index Low
    :param high: Index High
    :return: Index Of x
    """
    while low < high:
        mid = int((low + high) / 2)
        if list_nosize.elementAt(mid) > x:
            high = mid - 1
        elif list_nosize.elementAt(mid) < x:
            low = mid + 1
        else:
            return mid


if __name__ == '__main__':
    list_nosize = get_Listy()
    print(search(list_nosize, 156))
