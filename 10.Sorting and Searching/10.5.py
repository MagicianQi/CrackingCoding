# -*- coding: utf-8 -*-

"""
Question 10.5:
    Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find
                   the location of a given string.
    EXAMPLE
        Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
        Output: 4
"""


def search(strList, left, right, val):
    """
    Take O(n) time and O(1) space
    :param strList: String List
    :param left: Index Left
    :param right: Index Right
    :param val: Target val
    :return: Index Of Target
    """
    mid = int((left + right) / 2)
    if strList[mid] == val:
        return mid
    if left == right:
        return 0
    if strList[mid] == "":
        temp_l = mid - 1
        while left < mid:
            if strList[temp_l] == "" and temp_l > left:
                temp_l -= 1
            else:
                break
        temp_r = mid + 1
        while right > mid:
            if strList[temp_r] == "" and temp_r < right:
                temp_r += 1
            else:
                break
        return search(strList, left, temp_l, val) + search(strList, temp_r, right, val)


if __name__ == '__main__':
    str_list = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(search(str_list, 0, len(str_list) - 1, "car"))
