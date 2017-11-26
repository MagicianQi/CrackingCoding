# -*- coding: utf-8 -*-

"""
Question 1.2:
    Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""


def check_permutation_1(s, t):
    """
    Take O(nlogn) time and O(1) space
    :param s: String s
    :param t: String t
    :return: Result
    """
    if len(s) != len(t):
        return False
    s = ''.join(sorted(s, key=lambda x: ord(x)))
    t = ''.join(sorted(t, key=lambda x: ord(x)))
    if s == t:
        return True
    else:
        return False


def check_permutation_2(s, t):
    """
    Take O(n) time and O(1) space
    :param s: String s
    :param t: String t
    :return: Result
    """
    char_dict = {}
    for i in s:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    for j in t:
        if j not in char_dict:
            return False
        else:
            char_dict[j] -= 1
            if char_dict[j] < 0:
                return False
    return True


if __name__ == '__main__':
    result = check_permutation_1('cbaf', 'bcak')
    # result = check_permutation_2('cbaf', 'bcak')
    print(result)
