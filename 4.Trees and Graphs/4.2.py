# -*- coding: utf-8 -*-

"""
Question 4.2:
    Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
                  a binary search tree with minimal height.
"""


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def get_minimal_tree(array, start, end):
    """
    Take O(n) time and O(1) space
    :param array: Input Array
    :param start: Start Index
    :param end: End Index
    :return:
    """
    if start > end:
        return None
    mid = int((end + start) / 2)
    print(mid)
    node = Tree(array[mid])
    node.left = get_minimal_tree(array, start, mid - 1)
    node.right = get_minimal_tree(array, mid + 1, end)
    return node


if __name__ == '__main__':
    array = [1, 3, 6, 9, 13, 20]
    res = get_minimal_tree(array, 0, len(array) - 1)
    print('----')
