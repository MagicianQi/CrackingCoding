# -*- coding: utf-8 -*-

"""
Question 3.3:
    Stack of Plates: Imagine a stack of plates. if the stack gets too high, it might topple. Therefore, in real life,
                     we would likely start a mew stack when the previous stack exceeds some threshold. Implement a
                     data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
                     and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and
                     SetOfStacks.pop() should behave identically to a single stack(that is, pop() should return
                     the same values as it would if there were just a single stack).
"""


class SetOfStacks:
    def __init__(self, thresh):
        self.stacks = [[]]
        self.threshold = thresh
        self.index = 0

    def pop(self):
        """
        Take O(1) time
        :return: None
        """
        if len(self.stacks[self.index]) == 0:
            self.stacks.pop()
            self.index -= 1
            self.stacks[self.index].pop()
        else:
            self.stacks[self.index].pop()

    def push(self, val):
        """
        Take O(1) time
        :param val: Push value
        :return: None
        """
        if len(self.stacks[self.index]) == self.threshold:
            self.stacks.append([])
            self.stacks[self.index].append(val)
            self.index += 1
        else:
            self.stacks[self.index].append(val)


if __name__ == '__main__':
    s = SetOfStacks(3)
    s.push(2)
    s.push(5)
    s.push(6)
    s.push(128)
    s.push(245)
    s.push(89)
    s.push(8)
    s.push(0)
    s.pop()
    print(s.stacks)
