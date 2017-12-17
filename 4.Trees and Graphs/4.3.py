# -*- coding: utf-8 -*-

"""
Question 4.3:
    List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each
                    depth (.e.g, if you have a tree with depth D, you'll have D linked lists).
"""

import copy


class Tree:
    def __init__(self, val):
        self.val = val
        self.depth = None
        self.left = None
        self.right = None
        self.parent = None


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


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
    c.right = f
    e.right = g
    return a


def listOfDepth(root):
    """
    Take O(n) time and O(n) space
    :param root: Tree Root
    :return: List Of Depth
    """
    list_depth = []
    queue = Queue()
    flag = 1
    root.depth = 1
    queue.enqueue(root)
    temp = []
    while not queue.isEmpty():
        de = queue.dequeue()
        if flag == de.depth:
            temp.append(de.val)
        else:
            list_depth.append(copy.deepcopy(temp))
            temp.clear()
            flag += 1
            temp.append(de.val)
        if de.left:
            de.left.depth = de.depth + 1
            queue.enqueue(de.left)
        if de.right:
            de.right.depth = de.depth + 1
            queue.enqueue(de.right)
    list_depth.append(copy.deepcopy(temp))
    return list_depth


if __name__ == '__main__':
    root = get_tree()
    print(listOfDepth(root))
