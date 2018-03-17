#!/bin/python
import sys
def plusMinus(arr):
    # Complete This fuctio n
    arr_size = len(arr)
    print "%.5f" % (float(len([x for x in arr if x > 0]))/arr_size)
    print "%.5f" % (float(len([x for x in arr if x < 0]))/arr_size)
    print "%.5f" % (float(len([x for x in arr if x == 0]))/arr_size)

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)
