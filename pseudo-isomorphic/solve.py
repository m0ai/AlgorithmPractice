#!/bin/python

from __future__ import print_function

import os
import sys


def extractCases(s, r=2):
    print("Called extractCases Function with s : %s" % s)
    return

def remove_duplicate_pattern(list_data):
    print("Called remove_duplicate_pattern Function ")
    print(list_data)

    minimum = min(list_data)
    print(minimum)
    return

# a
# ab a

import math
def pseudoIsomorphicSubstrings(s):
    len_each_case = list()
    cases = set(list())
    for cur_index in range(1, len(s)+1):

        cases = set(list())
        splited_str = s[:cur_index]
        learned_pattern = list()


        str_len = len(splited_str)
        for read_length in range(1,str_len+1):
            for index in range(str_len):
                if index + read_length > str_len:
                    break


                char = splited_str[index:index+read_length]
                parsed_pattern = list()
                pattern_match_dict = {}
                new_pattern = 0
                for c in char:
                    if c not in pattern_match_dict:
                        pattern_match_dict[c] = new_pattern
                        new_pattern += 1
                    parsed_pattern.append(pattern_match_dict[c])

                if parsed_pattern not in learned_pattern:
                    learned_pattern.append(parsed_pattern)
                    cases.add(char)

        len_each_case.append(len(cases))
    return len_each_case


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = raw_input()

    s = "bbbbbcabccbabbbaaabcbaacbccaabbaacbccaababacccaabccaccbcaacbbbccccbcaaaaccacaccaabacaaaacabcbabaaabcb"

    result = pseudoIsomorphicSubstrings(s)

    '''
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    '''

