# -*- coding: utf-8 -*-

"""
Question 4.9:
    BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting
                   each element. Given a binary search tree with distinct elements, print all possible arrays that
                   could have led to this tree.
"""

import copy


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


def get_BST_Sequenecs(now):
    """
    Take O(n2) time and O(n2) space
    :param now: Selected Tree Node
    :return: None
    """
    wait = []
    temple = copy.deepcopy(now)
    for item in temple:
        if item.left:
            if item.left not in wait and item.left not in temple:
                wait.append(item.left)
        if item.right:
            if item.right not in wait and item.right not in temple:
                wait.append(item.right)
    if not len(wait):
        print([x.val for x in temple])
    for each in wait:
        temple.append(each)
        get_BST_Sequenecs(temple)
        temple.pop()


if __name__ == '__main__':
    get_BST_Sequenecs([get_tree()])
