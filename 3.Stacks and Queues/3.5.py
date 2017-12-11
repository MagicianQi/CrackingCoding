# -*- coding: utf-8 -*-

"""
Question 3.5:
    Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use a additional
                temporary stack, but you may not copy the elements into any other data structure(such as array). The
                stack supports the following operations: push, pop, peek and isEmpty.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            raise Exception('Pop Error!')
        return self.stack.pop()

    def push(self, val):
        self.stack.append(val)

    def peek(self):
        if self.isEmpty():
            raise Exception('Peek Error!')
        return self.stack[-1]

    def isEmpty(self):
        if not len(self.stack):
            return True
        else:
            return False


def sort_stack(s):
    """
    Take O(n2) time and O(n) space
    :param s: Stack To Sort
    :return: Sorted Stack
    """
    t = Stack()
    while not s.isEmpty():
        temp = s.pop()
        while not (t.isEmpty() or t.peek() >= temp):
            s.push(t.pop())
        t.push(temp)
    return t


if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(3)
    s.push(1)
    s.push(5)
    s.push(4)
    res = sort_stack(s)
    print(res.pop())
    print(res.pop())
    print(res.pop())
    print(res.pop())
    print(res.pop())

