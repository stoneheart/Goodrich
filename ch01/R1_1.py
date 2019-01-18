#!/usr/bin/env python
#
#    File Name:  R1_1.py
#    Created By: Kun Zheng (kz9892@gmail.com)
#    Created On: 2019-01-18
#    Last Modified: 2019-01-18 15:24:47
#
#    Description:
#

def is_multiple(n, m):
    """Take interger values n and m
    Returns True if n is a multiple of m and False otherwise

    :n: <int>
    :m: <int>
    :returns: <bool>

    """
    return n % m == 0

if __name__ == "__main__":
    print("10 is a multiple of 2: ", is_multiple(10, 2))
    print("10 is a multiple of 3: ", is_multiple(10, 3))
