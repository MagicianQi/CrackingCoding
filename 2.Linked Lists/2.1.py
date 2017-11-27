# -*- coding: utf-8 -*-

"""
Question 2.1:
    Remove Dups: Write code to remove duplicates from an unsorted linked list.
                 FOLLOW UP
                 How would you solve this problem if temporary buffer is not allowed.

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


def removeDups(linkedList):
    """
    Take O(n) time and O(n) space
    :param linkedList: Input LinkedList
    :return: Output linkedList
    """
    temp = []
    previous = linkedList
    while linkedList:
        if linkedList.val not in temp:
            temp.append(linkedList.val)
            previous = linkedList
        else:
            previous.next = linkedList.next
        linkedList = linkedList.next
    return linkedList


def removeDups_no_buffer(linkedList):
    """
    Take O(n2) time and O(1) space
    :param linkedList: Input LinkedList
    :return: Output linkedList
    """
    current = linkedList
    while current:
        runner = current
        while runner.next:
            if current.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return linkedList


if __name__ == '__main__':
    linkedList = Node(1, Node(2, Node(3, Node(5, Node(3, Node(2, None))))))
    printList(linkedList)
    print('------------')
    removeDups_no_buffer(linkedList)
    printList(linkedList)
    print('------------')
