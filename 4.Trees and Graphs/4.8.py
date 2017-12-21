# -*- coding: utf-8 -*-

"""
Question 4.8:
    First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a
                           binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
                           necessarily a binary search tree.
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
    return [a, b, c, d, e, f, g]


def get_first_ancestor(p, q):
    """
    Take O(n2) time and O(1) space
    :param p: Tree Node p
    :param q: Tree Node q
    :return: Tree Node Ancestor
    """
    temp_p = p
    while temp_p.parent:
        temp_p = temp_p.parent
        temp_q = q
        while temp_q.parent:
            temp_q = temp_q.parent
            if temp_p == temp_q:
                return temp_p
    return None


def get_first_ancestor_no_parent(root, p, q):
    """
    Take O(n) time and O(1) space
    :param root: Tree Node Root
    :param p: Tree Node p
    :param q: Tree Node q
    :return: Tree Node Ancestor
    """
    if not (root or root.left or root.right):
        return None
    if root == p or root == q:
        return None
    if p in [root.left, root.right] or q in [root.left, root.right]:
        return root
    if covers(root.left, p) and covers(root.left, q):
        return get_first_ancestor_no_parent(root.left, p, q)
    elif covers(root.right, p) and covers(root.right, q):
        return get_first_ancestor_no_parent(root.right, p, q)
    else:
        return root


def covers(root, p):
    """
    Take O(n) time and O(1) space
    :param root: Tree Node Root
    :param p: Tree Node p
    :return: Result (Whether Root covers p)
    """
    if not root:
        return False
    if root == p:
        return True
    return covers(root.left, p) or covers(root.right, p)


if __name__ == '__main__':
    nodes = get_tree()
    ancestor = get_first_ancestor(nodes[1], nodes[3])
    print(ancestor.val)
    ancestor_no_parent = get_first_ancestor_no_parent(nodes[0], nodes[1], nodes[3])
    print(ancestor_no_parent.val)
