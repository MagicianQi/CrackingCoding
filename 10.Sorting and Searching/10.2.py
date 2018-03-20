# -*- coding: utf-8 -*-

"""
Question 10.2:
    Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
                    each other.
"""


def anagram_compare(s1, s2):
    """
    Take O(n2) time and O(1) space
    :param s1: String s1
    :param s2: String s2
    :return: Compare Result
    """
    if s1 == s2:
        return True
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


def anagram_group_sort(stringList):
    """
    Take O(n2) time and O(1) space
    :param stringList: String List
    :return: None
    """
    length = len(stringList)
    op_1 = 0
    while op_1 < length:
        for i in range(op_1 + 1, length):
            if anagram_compare(stringList[op_1], stringList[i]):
                temp = stringList[op_1 + 1]
                stringList[op_1 + 1] = stringList[i]
                stringList[i] = temp
                op_1 += 1
        op_1 += 1


if __name__ == '__main__':
    strList = ['aabb', 'qwe', 'iop', 'weq', 'abab', 'poi']
    print(strList)
    anagram_group_sort(strList)
    print(strList)
