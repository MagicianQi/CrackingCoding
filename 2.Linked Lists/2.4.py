# -*- coding: utf-8 -*-

"""
Question 2.4:
    Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
               before all nodes greater than or equal to x. if x is contained within the list, the values of
               x only need to be after the elements less than x(see below). The partition element x can appear
               anywhere in the "right partition";it does not need to appear between the left and right partitions.
    EXAMPLE:
        Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
        Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
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
        print(linkedList.val)
        linkedList = linkedList.next


def partition(linkedList, thresh):
    """
    Take O(n) time and O(1) space
    :param linkedList: Input LinkedList
    :param thresh: Partition Threshold
    :return: Output LinkedList
    """
    head = None
    tail = None
    while linkedList:
        next_t = linkedList.next
        if linkedList.val < thresh:
            linkedList.next = head
            head = linkedList
        else:
            linkedList.next = tail
            tail = linkedList
        linkedList = next_t
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = tail
    return head


if __name__ == '__main__':
    linkedList = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1, None)))))))
    printList(partition(linkedList, 5))
