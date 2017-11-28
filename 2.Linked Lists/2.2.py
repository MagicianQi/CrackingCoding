# -*- coding: utf-8 -*-

"""
Question 2.2:
    Return Kth to last: Implement an algorithm to find the kth to last element of a singly linked list.
"""


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def printKthToLast(linkedList, k):
    """
    Take O(n) time and O(1) space
    :param linkedList: Input LinkedList
    :param k: Kth To Last
    :return: None
    """
    length = 0
    head_count = linkedList
    while head_count:
        length += 1
        head_count = head_count.next
    pos = length - k
    head = linkedList
    while head:
        head = head.next
        pos -= 1
        if pos == 0:
            print(head.val)


def printKthToLast_recursive(linkedList, k):
    """
    Take O(n) time and O(n) space
    :param linkedList: Input LinkedList
    :param k: Kth To Last
    :return: Count To Last
    """
    if not linkedList:
        return 0
    index = printKthToLast_recursive(linkedList.next, k) + 1
    if index == k:
        print(linkedList.val)
    return index


def printKthToLast_iter(linkedList, k):
    """
    Take O(n) time and O(1) space
    :param linkedList: Input LinkedList
    :param k: Kth To Last
    :return: None
    """
    p1 = linkedList
    p2 = linkedList
    while k > 0:
        k -= 1
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    print(p2.val)


if __name__ == '__main__':
    linkedList = Node(1, Node(2, Node(3, Node(5, Node(3, Node(2, None))))))
    printKthToLast(linkedList, 3)
    print('----------')
    printKthToLast_recursive(linkedList, 3)
    print('----------')
    printKthToLast_iter(linkedList, 3)
    print('----------')
