# -*- coding: utf-8 -*-

"""
Question 4.5:
    Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_tree():
    a = Tree(4)
    b = Tree(2)
    c = Tree(6)
    d = Tree(1)
    e = Tree(3)
    f = Tree(5)
    g = Tree(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    return a


def tree2array(tree, array):
    """
    Take O(n) time and O(1) space
    :param tree: Tree Root
    :param array: To Array
    :return: None
    """
    if not tree:
        return
    tree2array(tree.left, array)
    array.append(tree.val)
    tree2array(tree.right, array)


def checkBST(array):
    """
    Take O(n) time and O(n) space
    :param array: Input Array
    :return: Result
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


if __name__ == '__main__':
    arr = []
    tree2array(get_tree(), arr)
    print(arr)
    print(checkBST(arr))
