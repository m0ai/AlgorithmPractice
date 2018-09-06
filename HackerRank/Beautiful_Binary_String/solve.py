#!/bin/python

import sys

def beautifulBinaryString(b):
    # Complete this function
    return b.count("010")

if __name__ == "__main__":
    n = int(raw_input().strip())
    b = raw_input().strip()
    result = beautifulBinaryString(b)
    print result

