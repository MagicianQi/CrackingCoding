"""
Question 2.8:
    Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
                    beginning of the loop.
    EXAMPLE:
        Input:  A -> B -> C -> D -> E -> C [the same C as earlier]
        Output: C
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
    i = 0
    while linkedList:
        i += 1
        if i > 20:
            break
        print(linkedList.val, end=' ')
        linkedList = linkedList.next
    print('...', end=' ')


def loopDetection_1(linkedList):
    """
    Take O(n) time and O(1) space
    :param linkedList: Input LinkedList
    :return: Loop
    """
    slow = linkedList
    fast = linkedList
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if not(fast or fast.next):
        return False, 0
    slow = linkedList
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return True, fast


if __name__ == '__main__':
    list = Node(1, Node(2, Node(3,  Node(4, Node(5, Node(6, Node(7,  Node(8, None))))))))
    loop = list
    while loop.next:
        loop = loop.next
    loop.next = list.next.next.next
    printList(list)
    print('\n--------------------------------------------')
    result = loopDetection_1(list)
    print(str(result[0]) + '\t' + str(result[1].val), end=' ')
    print('\n--------------------------------------------')
