#!/bin/python

import sys


def diagonalDifference(a):
    # Complete this function
    primary = secondary = int()
    for index, array in enumerate(a):
        primary += array[index]
        secondary += array[-index-1]
    return abs(primary-secondary)

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []

    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(a)
    print result

