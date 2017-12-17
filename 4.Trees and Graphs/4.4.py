# -*- coding: utf-8 -*-

"""
Question 4.4:
    Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, a
                    balanced tree is defined to be a tree such that he heights of the two subtrees of any node never
                    differ by more than one.
"""


class Tree:
    def __init__(self, val):
        self.val = val
        self.height = None
        self.left = None
        self.right = None


def get_tree():
    a = Tree(1)
    b = Tree(2)
    c = Tree(3)
    d = Tree(4)
    e = Tree(5)
    f = Tree(6)
    g = Tree(7)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    d.right = f
    f.right = g
    return a


def getHeight(tree):
    """
    Take O(n) time and O(1) space
    :param tree: Tree Root
    :return: Tree Height
    """
    if not tree:
        return 0
    if not tree.height:
        tree.height = max(getHeight(tree.left), getHeight(tree.right)) + 1
    return tree.height


def isBalanced(tree):
    """
    Take O(nlogn) time and O(n) space
    :param tree: Tree Root
    :return: isBalanced
    """
    if not tree:
        return True
    diff = abs(getHeight(tree.left) - getHeight(tree.right))
    if diff > 1:
        return False
    else:
        return isBalanced(tree.left) and isBalanced(tree.right)


if __name__ == '__main__':
    print(isBalanced(get_tree()))
