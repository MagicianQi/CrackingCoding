"""
Question 2.5:
    Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits
               are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that
               adds the two numbers and returns the sum as a linked list.
    EXAMPLE:
        Input: (6 -> 1 -> 7) + (2 -> 9 ->5). That is, 617 + 295.
        Output:(9 -> 1 - 2). That is 912
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


def addLists(l1, l2):
    """
    Take O(m + n) time and O(m + n) space
    :param l1: Input LinkedList l1
    :param l2: Input LinkedList l2
    :return: Output LinkedList
    """
    num_1 = ''
    num_2 = ''
    while l1:
        num_1 += str(l1.val)
        l1 = l1.next
    while l2:
        num_2 += str(l2.val)
        l2 = l2.next
    s_data = list(*zip(*str(int(num_1) + int(num_2))))
    result = Node(0, None)
    temp = result
    for s in s_data:
        temp.next = Node(int(s), None)
        temp = temp.next
    return result.next


if __name__ == '__main__':
    l1 = Node(6, Node(1, Node(7, None)))
    l2 = Node(2, Node(9, Node(5, None)))
    printList(l1)
    print('\n-----------')
    printList(l2)
    print('\n-----------')
    result = addLists(l1, l2)
    printList(result)
    print('\n-----------')