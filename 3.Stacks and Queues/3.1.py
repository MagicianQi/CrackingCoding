# -*- coding: utf-8 -*-

"""
Question 3.1:
    Three in one: Describe how you could use a single array to implement three stacks.
"""

import numpy as np

import random


class Array2Stack:
    def __init__(self, length):
        self.array = np.arange(length)
        self.length = length
        self.stack_1 = [0, 0]   # stack[0]: ptr, stack[1]: stack length
        self.stack_2 = [random.randint(0, length), 0]
        self.stack_3 = [random.randint(self.stack_2[0], length), 0]

    def pop(self, num):
        """
        Take O(n) time and O(1) space
        :param num: Stack Number
        :return: None
        """
        if num == 1:
            if self.stack_1[0] <= 0:
                raise Exception('Pop Out Of Bounds')
            self.stack_1[0] -= 1
            self.stack_1[1] -= 1
        elif num == 2:
            if self.stack_2[0] <= self.stack_1[0]:
                raise Exception('Pop Out Of Bounds')
            self.stack_2[0] -= 1
            self.stack_2[1] -= 1
        elif num == 3:
            if self.stack_3[0] <= self.stack_2[0]:
                raise Exception('Pop Out Of Bounds')
            self.stack_3[0] -= 1
            self.stack_3[1] -= 1
        else:
            print('Pop Error')

    def push(self, num, val):
        """
        Take O(n) time and O(1) space
        :param num: Stack Number
        :param val: Push Value
        :return: None
        """
        if num == 1:
            if self.stack_1[0] >= (self.stack_2[0] - self.stack_2[1]):
                raise Exception('Push Out Of Bounds')
            self.array[self.stack_1[0]] = val
            self.stack_1[0] += 1
            self.stack_1[1] += 1
        elif num == 2:
            if self.stack_2[0] >= (self.stack_3[0] - self.stack_3[1]):
                raise Exception('Push Out Of Bounds')
            self.array[self.stack_2[0]] = val
            self.stack_2[0] += 1
            self.stack_2[1] += 1
        elif num == 3:
            if self.stack_3[0] >= self.length:
                raise Exception('Push Out Of Bounds')
            self.array[self.stack_3[0]] = val
            self.stack_3[0] += 1
            self.stack_3[1] += 1
        else:
            print('Push Error')

    def printStack(self, num):
        """
        Take O(n) time and O(1) space
        :param num: Stack Number
        :return: None
        """
        if num == 1:
            print(self.array[0:self.stack_1[0]])
        elif num == 2:
            print(self.array[(self.stack_2[0] - self.stack_2[1]):self.stack_2[0]])
        elif num == 3:
            print(self.array[(self.stack_3[0] - self.stack_3[1]):self.stack_3[0]])
        else:
            print('Print Stack Error')

    def printArray(self):
        print(self.array[:])


if __name__ == '__main__':
    s = Array2Stack(100)
    s.push(1, 2)
    s.push(1, 3)
    s.push(2, 10)
    s.push(3, 5)
    s.push(2, 17)
    s.push(3, 56)
    s.push(2, 89)
    s.push(3, 52)
    s.printStack(1)
    s.printStack(2)
    s.printStack(3)
    s.pop(1)
    s.pop(2)
    s.pop(3)
    print('-------------')
    s.printStack(1)
    s.printStack(2)
    s.printStack(3)
    print('-------------')
