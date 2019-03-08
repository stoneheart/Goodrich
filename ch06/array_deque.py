#!/usr/bin/env python
#
#    File Name:  array_deque.py
#    Created By: Kun Zheng (kz9892@gmail.com)
#    Created On: 2019-02-11
#    Last Modified: 2019-02-12 10:50:56
#
#    Description:
#

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exceptions import Empty

class ArrayDeque:
    """Double-Ended Queue implementation using a Pythong list as underlying
    storage."""
    DEFAULT_CAPACITY = 10                       # moderate capacity for all new deques

    def __init__(self):
        """Create an empty deque."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the first element of deque.

        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the last element of deque.

        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def _resize(self, cap):
        """Resize to a new list of capacity."""
        old = self._data                        # keep track of existing list
        self._data = [None] * cap               # allocate list with new capacity
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]           # only consider existing elements
            walk = (1 + walk) % len(old)        # intentionally shift indices
        self._front = 0                         # front has been realigned

    def delete_first(self):
        """Remove and return the first element from deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None          # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        """Remove and return the last element from deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None                 # help garbage collection
        self._size -= 1
        return answer

    def add_last(self, e):
        """Add element e to the back of deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        """Add element e to the front of deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))   # double the array size
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

if __name__ == '__main__':
    D = ArrayDeque()            # contents: []
    D.add_last(5)               # contents: [5]
    D.add_first(3)              # contents: [3, 5]
    D.add_first(7)              # contents: [7, 3, 5]
    print(D.first())            # contents: [7, 3, 5];  output 7
    print(D.delete_last())      # contents: [7, 3];     output 5
    print(len(D))               # contents: [7, 3];     output 2
    print(D.delete_last())      # contents: [7];        output 3
    print(D.delete_last())      # contents: [];         output 7
    D.add_first(6)              # contents: [6]
    print(D.last())             # contents: [6];        output 6
    D.add_first(8)              # contents: [8, 6]
    print(D.is_empty())         # contents: [8, 6];     output False
    print(D.last())             # contents: [8, 6];     output 6

