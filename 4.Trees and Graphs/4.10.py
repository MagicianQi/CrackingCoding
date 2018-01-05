# -*- coding: utf-8 -*-

"""
Question 4.10:
    Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to
                   determine if T2 is a subtree of T1.
                   A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical
                   to T2. That is, if you cut off the tree at node n, the two trees would be identical.
"""


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_tree_1():
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


def get_tree_2():
    a = Tree(2)
    b = Tree(1)
    c = Tree(3)
    a.left = b
    a.right = c
    return a


def subTree(t1, t2):
    """
    Take O(n) time and O(1) space
    :param t1: Tree t1
    :param t2: Tree t2
    :return: Result
    """
    if not t1:
        return False
    elif t1.val == t2. val and matchTree(t1, t2):
        return True
    else:
        return subTree(t1.left, t2) or subTree(t1.right, t2)


def matchTree(t1, t2):
    """
    Take O(n) time and O(1) space
    :param t1: Tree t1
    :param t2: Tree t2
    :return: Result
    """
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right)


if __name__ == '__main__':
    print(subTree(get_tree_1(), get_tree_2()))
