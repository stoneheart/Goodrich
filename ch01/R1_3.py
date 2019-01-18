#!/usr/bin/env python
#
#    File Name:  R1_3.py
#    Created By: Kun Zheng (kz9892@gmail.com)
#    Created On: 2019-01-18
#    Last Modified: 2019-01-18 15:53:40
#
#    Description:
#

def minmax(data):
    """Takes a sequence of one or more numbers
    Returns the smallest and largest numbers in a tuple

    :data: numeric iterable
    :returns: min and max of input data

    """
    data_min = data_max = data[0]
    for d in data:
        if d < data_min:
            data_min = d
        if d > data_max:
            data_max = d
    return data_min, data_max

if __name__ == "__main__":
    data = [5, 4, 3, 2]
    d_min, d_max = minmax(data)
    print("Test data sequence is: ", data)
    print("The min is {} and max is {}".format(d_min, d_max))
