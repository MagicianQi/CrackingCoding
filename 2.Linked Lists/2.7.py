"""
Question 2.7:
    Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
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


def getIntersection(linkedList_1, linkedList_2):
    """
    Take O(n) time and O(1) space
    :param linkedList_1: Input LinkedList 1
    :param linkedList_2: Input LinkedList 2
    :return: Intersection
    """
    length_1 = 1
    length_2 = 1
    temp_1 = linkedList_1
    temp_2 = linkedList_2
    while temp_1.next:
        length_1 += 1
        temp_1 = temp_1.next
    while temp_2.next:
        length_2 += 1
        temp_2 = temp_2.next
    if temp_1 != temp_2:
        return False, None
    if length_1 > length_2:
        long = linkedList_1
        slow = linkedList_2
    else:
        long = linkedList_2
        slow = linkedList_1
    for i in range(abs(length_1 - length_2)):
        long = long.next
    while long:
        if long.next == slow.next:
            return True, long.next.val
        long = long.next
        slow = slow.next
    return False, None


if __name__ == '__main__':
    intersection = Node(7, Node(2, Node(1,  None)))
    list_1 = Node(3, Node(1, Node(5,  Node(9,  intersection))))
    list_2 = Node(4, Node(6, intersection))
    printList(list_1)
    print('\n-------------')
    printList(list_2)
    print('\n-------------')
    result = getIntersection(list_1, list_2)
    print(str(result[0]) + '\t' + str(result[1]), end=' ')
    print('\n-------------')
