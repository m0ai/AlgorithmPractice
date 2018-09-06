#!/usr/bin/python2

import string

def print_rangoli(size):
    if 0 < size and size > 27:
        return -1
    print (size)
    mid = size - 1
    table = list()

    for i in range(size-1, 0, -1):
        row = ['-'] * (size * 2 - 1)
        for j in range(size-i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))

    for i in range(size):
        row = ['-'] * (size * 2 - 1)
        for j in range(size-i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))

if __name__ == '__main__':
    print_rangoli(5)
