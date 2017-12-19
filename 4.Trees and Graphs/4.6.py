# -*- coding: utf-8 -*-

"""
Question 4.6:
    Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary
               search tree. You may assume that each node has a link to its parent.
"""


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def get_tree():
    a = Tree(4)
    b = Tree(2)
    c = Tree(6)
    d = Tree(1)
    e = Tree(3)
    f = Tree(5)
    g = Tree(7)

    a.left = b
    b.parent = a

    a.right = c
    c.parent = a

    b.left = d
    d.parent = b

    b.right = e
    e.parent = b

    c.left = f
    f.parent = c

    c.right = g
    g.parent = c
    return a


def get_next(tree_node):
    """
    Take O(n) time and O(1) space
    :param tree_node: Input Tree Node
    :return: Next Node
    """
    if tree_node.right:
        temp = tree_node.right
        while temp.left:
            temp = temp.left
        return temp
    elif tree_node.parent.left == tree_node:
        return tree_node.parent
    else:
        return None


if __name__ == '__main__':
    node = get_next(get_tree())
    print(node.val)
