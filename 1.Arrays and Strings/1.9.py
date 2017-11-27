# -*- coding: utf-8 -*-

"""
Question 1.9:
    String Rotation: Assume you have a method isSubString which checks if one word is substring of another.
                     Given two strings, s1 and s2, write code to check if s2 is rotation of s1 using only one
                     call to isSubstring(e.g.,"waterbottle" is a rotation of "erbottlewat")
"""


def isRotation(s1, s2):
    """
    Take O(n) time and O(n) space
    :param s1: Input String s1
    :param s2: Input String s2
    :return: result
    """
    return isSubString(s1 + s1, s2)


def isSubString(s1, s2):
    """
    Take O(n1) time and O(n) space
    :param s1: Input String s1
    :param s2: Input String s2
    :return: result
    """
    if s2 in s1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isRotation('erbottlewat', 'waterbottle'))