#!/bin/python
# -- challenges link --
# hackerrank.com/challenges/pseudo-isomorphic-substrings/problem
#
# - summary
#
# you are given a string S, consisting of no more than 105
# lowercase alphabetical characters. For every prefix of S
# denoted by S', you are expected to find the size of
# the largest possible set of strings ,
# such that all elements of the set are substrings of S'
# and no two strings inside the set are pseudo-isomorphic to each other.

from __future__ import print_function

import os
import sys

def pseudoIsomorphicSubstrings(s):
    learned_pattern = list()
    for cur_index in range(1, len(s)+1):
        splited_str = s[:cur_index]
        for read_length in reversed(range(cur_index)):
            char = splited_str[read_length:cur_index]

            parsed_pattern = list()
            pattern_match_dict = {}
            new_char = 0
            for c in char:
                if c not in pattern_match_dict:
                    pattern_match_dict[c] = new_char
                    new_char += 1
                parsed_pattern.append(pattern_match_dict[c])

            if parsed_pattern not in learned_pattern:
                learned_pattern.append(parsed_pattern)

        yield len(learned_pattern)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #s = raw_input()
    s = "bbbbbcabccbabbbaaabcbaacbccaabbaacbccaababacccaabccaccbcaacbbbccccbcaaaaccacaccaabacaaaacabcbabaaabcb"
    result = pseudoIsomorphicSubstrings(s)

    # for solving
    '''
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    '''

