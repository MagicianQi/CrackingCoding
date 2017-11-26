# -*- coding: utf-8 -*-

"""
Question 1.5:
    Given two strings, write a function to check if they are one edit(or zero edits) away.
    edit: insert a character, remove a character, replace a character.
"""


def checkOneEdit(s1, s2):
    """
    Take O(n) time and O(n) space
    :param s1: String first
    :param s2: String second
    :return: result
    """
    length_diff = abs(len(s1) - len(s2))
    if length_diff >= 2:
        return False
    elif length_diff == 1:
        op_count = 0
        if len(s1) > len(s2):
            long = s1
            short = s2
        else:
            long = s2
            short = s1
        for i in range(len(short)):
            if long[i+op_count] != short[i]:
                op_count += 1
        if op_count > 1:
            return False
        else:
            return True
    elif length_diff == 0:
        op_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                op_count += 1
        if op_count > 1:
            return False
        else:
            return True
    else:
        return False
    pass


if __name__ == '__main__':
    print(checkOneEdit('ac', 'bcd'))
