# -*- coding: utf-8 -*-

"""
Question 3.2:
    Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the
               minimum element? Push, pop and min should all operate in O(1) time.
"""


class Stack:
    def __init__(self):
        """
        Take O(n) space
        """
        self.min = []
        self.stack = []

    def push(self, val):
        """
        Take O(1) time
        :param val: Push value
        :return: None
        """
        self.stack.append(val)
        if len(self.min):
            if val < self.min[-1]:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self):
        """
        Take O(1) time
        :return: None
        """
        self.stack.pop()
        self.min.pop()

    def cal_min(self):
        """
        Take O(1) time
        :return: None
        """
        print(self.min[-1])


if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(3)
    s.push(1)
    s.push(10)
    s.pop()
    s.pop()
    s.cal_min()
