#!/bin/python

import sys

def miniMaxSum(arr):
    # Complete this function
    arr_sum = sum(arr)
    # Print Mini Sum and Max sum
    print arr_sum - min(arr), arr_sum - max(arr)

if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    miniMaxSum(arr)



