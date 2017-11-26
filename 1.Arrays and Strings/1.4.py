# -*- coding: utf-8 -*-

"""
Question 1.4:
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
"""


def palindrome_permutation(s):
    """
    Take O(n) time and O(1) space
    :param s: String s
    :return: Result
    """
    char_dict = {}
    for i in s:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    numOdd = 0
    for key in char_dict:
        if key != ' ':
            if char_dict[key] % 2 == 1:
                numOdd += 1
    if numOdd < 2:
        print_permutation(char_dict)
        return True
    else:
        return False


def print_permutation(char_dict):
    mid = ''
    p_list = []
    candidates = ''
    for key in char_dict:
        if char_dict[key] % 2 == 1:
            mid = mid + key
            char_dict[key] -= 1
        else:
            for i in range(int(char_dict[key] / 2)):
                candidates += key
    get_permutation('', candidates, p_list)
    for p in p_list:
        print(p + mid + p[::-1])


def get_permutation(select, string, p_list):
    if len(string) == 1:
        if (select + string) not in p_list:
            p_list.append(select + string)
    for i in range(len(string)):
        temp = select + string[i]
        get_permutation(temp, string[:i] + string[i+1:], p_list)


if __name__ == '__main__':
    result = palindrome_permutation('dwadwcafawfaw')
    print(result)
