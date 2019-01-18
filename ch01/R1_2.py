#!/usr/bin/env python
#
#    File Name:  R1_2.py
#    Created By: Kun Zheng (kz9892@gmail.com)
#    Created On: 2019-01-18
#    Last Modified: 2019-01-18 15:17:43
#
#    Description:
#

def is_even(k):
    """Takes an integer value and returns True
    if k is even and False otherwise

    :k: <int>
    :returns: <bool>

    """
    return k & 1 == 0

if __name__ == "__main__":
    print("10 is even: ", is_even(10))
    print("7 is even: ", is_even(7))
