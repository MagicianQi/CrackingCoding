# -*- coding: utf-8 -*-

"""
Question 1.6:
    String Compression : Implement a method to perform basic string compression using the counts of repeated characters.
    For example : aabcccccaaa -> a2b1c5a3
"""


def strCompression(s):
    """
    Take O(n) time and O(n) space
    :param s: Input String
    :return: Output String
    """
    letter = ''
    count = 1
    result = ''
    for i in s:
        if letter != i:
            letter = i
            result += str(count)
            result += i
            count = 1
        else:
            count += 1
    result += str(count)
    return result[1:]


if __name__ == '__main__':
    print(strCompression('aaabbccccc'))
