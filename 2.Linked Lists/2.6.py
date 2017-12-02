"""
Question 2.6:
    Palindrome: Implement a function to check if a linked list is a palindrome.
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


def isPalindrome(linkedList):
    """
    Take O(n) time and O(n) space
    :param linkedList: Input LinkedList
    :return: Result
    """
    stack = []
    slow = linkedList
    fast = linkedList
    num_flag = 0
    while fast:
        stack.append(slow.val)
        slow = slow.next
        if not fast.next:
            num_flag = 1
            break
        fast = fast.next.next
    if num_flag:
        stack.pop()
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True


if __name__ == '__main__':
    linkedList = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1, None))))))
    print(isPalindrome(linkedList))
