#!/bin/python3
import sys
st_start_p, st_jump_distance, nd_start_p, nd_jump_distance = map(int, input().strip().split(' '))
duplicated_kgr_locaiton = "NO"
if st_jump_distance > nd_jump_distance and st_start_p <= nd_start_p:
    st_it = iter(range(st_start_p, sys.maxsize, st_jump_distance))
    nd_it = iter(range(nd_start_p, sys.maxsize, nd_jump_distance))
    for step in range(100000):
        a = next(st_it)
        b = next(nd_it)
        if a == b:
            duplicated_kgr_locaiton = "YES"
            break
print (duplicated_kgr_locaiton)
