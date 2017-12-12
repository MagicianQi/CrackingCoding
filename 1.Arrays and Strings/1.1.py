# -*- coding: ascii -*-

"""
Question 1.1:
    Is Unique : Implement an algorithm to determine if a string has all unique characters.
                What if you cannot use additional data structures?
"""

from bitarray import bitarray


def is_unique(inputString):
    """
    Take O(n) time and O(1) space
    :param inputString: Input String
    :return: Result
    """
    if len(inputString) > 128:
        return False
    char_list = []
    for char in inputString:
        if char in char_list:
            return False
        char_list.append(char)
    return True


def is_unique_no_add(inputString):
    """
    Take O(n2) time and O(1) space
    :param inputString: Input String
    :return: Result
    """
    if len(inputString) > 128:
        return False
    for i in range(len(inputString)):
        for j in inputString[:i] + inputString[i+1:]:
            if inputString[i] == j:
                return False
    return True


def is_unique_no_add_bit(inputString):
    """
    Take O(n) time and O(1) space
    :param inputString: Input String
    :return: Result
    """
    if len(inputString) > 128:
        return False
    char_set = bitarray(128)
    char_set.setall(0)
    for char in inputString:
        if char_set[ord(char)] == 1:
            return False
        char_set[ord(char)] = 1
    return True


if __name__ == '__main__':
    result = is_unique('pkubsma')
    # result = is_unique_no_add('pkubsma')
    # result = is_unique_no_add_bit('pkubsma')
    print(result)
