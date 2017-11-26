# -*- coding: utf-8 -*-

"""
Question 1.3:
    URLify: Write a method to replace all spaces in a string with '%20'.
"""


def replace_spaces(s, trueLength):
    """
    Take O(n) time and O(1) space
    :param s: String s
    :param trueLength: True Length of s
    :return: String after replace spaces
    """
    return s[:trueLength].replace(' ', '%20')


if __name__ == '__main__':
    result = replace_spaces('Mr John Smith    ', 13)
    print(result)
