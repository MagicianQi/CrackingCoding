# -*- coding: utf-8 -*-

"""
Question 2.3:
    Delete Middle Node: Implement an algorithm to delete a node in the middle(i.e., any node but the first
                        and the last node, not necessarily thr exact middle)of a single linked list, given
                        only access to that node.
"""


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def printList(linkedList):
    """
    Print linkedList
    :param linkedList: Input LinkedList
    :return: None
    """
    while linkedList:
        print(linkedList.val, end=' ')
        linkedList = linkedList.next


def delNode(linkedList):
    """
    Take O(1) time and O(1) space
    :param linkedList: Input LinkedList
    :return: If Can Delete Node
    """
    if not (linkedList or linkedList.next):
        return False
    linkedList.val = linkedList.next.val
    linkedList.next = linkedList.next.next
    return True


if __name__ == '__main__':
    linkedList = Node(1, Node(2, Node(3, Node(5, Node(3, Node(2, None))))))
    ptr = linkedList.next.next
    printList(linkedList)
    print('\n-----------')
    delNode(ptr)
    printList(linkedList)
    print('\n-----------')
