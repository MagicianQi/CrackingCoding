# -*- coding: utf-8 -*-

"""
Question 4.12:
    Paths with Sum: You are given a binary tree in which each node contains an integer value(which might be positive or
                    negative). Design an algorithm to count the number of paths that sum to a given value. The path does
                    not need to start or end at the root or a leaf, but it must go downwards(traveling only from parent
                    nodes to child nodes).
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


def count_sum(tree, target_sum):
    """
    Take O(n) time and O(1) space
    :param tree: Tree Root
    :param target_sum: Target Value
    :return: Total Paths
    """
    if not tree:
        return 0
    root_sum = count_sum_from_node(tree, target_sum, 0)
    return count_sum(tree.left, target_sum) + count_sum(tree.right, target_sum) + root_sum


def count_sum_from_node(tree, target_sum, current_sum):
    """
    Take O(n) time and O(1) space
    :param tree: Tree Root
    :param target_sum: Target Value
    :param current_sum: Current Sum Value
    :return: Current Node Total Paths
    """
    if not tree:
        return 0
    current_sum += tree.val
    total_paths = 0
    if target_sum == current_sum:
        total_paths += 1
    total_paths += count_sum_from_node(tree.left, target_sum, current_sum)
    total_paths += count_sum_from_node(tree.right, target_sum, current_sum)
    return total_paths


if __name__ == '__main__':
    print(count_sum(get_tree(), 11))
