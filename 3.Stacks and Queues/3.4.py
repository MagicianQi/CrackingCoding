# -*- coding: utf-8 -*-

"""
Question 3.4:
    Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""


class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def in_queue(self, val):
        """
        Take O(1) time
        :param val: InQueue Value
        :return: None
        """
        print('In : ' + str(val))
        self.stack_in.append(val)

    def de_queue(self):
        """
        Take O(n) time
        :return: None
        """
        if len(self.stack_out) == 0:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            print('Out : ' + str(self.stack_out.pop()))
        else:
            print('Out : ' + str(self.stack_out.pop()))


if __name__ == '__main__':
    q = MyQueue()
    q.in_queue(3)
    q.in_queue(34)
    q.in_queue(10)
    q.in_queue(8)
    q.de_queue()
    q.de_queue()
    q.de_queue()
    print(q.stack_in)
    print(q.stack_out)

