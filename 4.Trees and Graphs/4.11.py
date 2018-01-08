# -*- coding: utf-8 -*-

"""
Question 4.11:
    Random Node: You are implementing a binary search tree class from scratch, which, in addition to insert, find, and
                 delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be
                 equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you
                 would implement the rest of the methods.
"""

import random


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


def traverse(t, treelist):
    """
    Take O(n) time and O(n) space
    :param t: Tree Root t
    :param treelist: Tree ListTake O(n) time and O(1) space
    :return: None
    """
    if not t:
        return
    traverse(t.left, treelist)
    treelist.append(t.val)
    traverse(t.right, treelist)


def getRondomNode_1(t):
    """
    Take O(n) time and O(n) space
    :param t: Tree Root t
    :return: None
    """
    treelist = []
    traverse(t, treelist)
    random_num = random.randint(0, len(treelist) - 1)
    return treelist[random_num]


if __name__ == '__main__':
    print(getRondomNode_1(get_tree()))
