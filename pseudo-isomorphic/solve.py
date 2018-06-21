#!/bin/python


# challenges link  - www.hackerrank.com/challenges/pseudo-isomorphic-substrings/problem

from __future__ import print_function


import os
import sys
def pseudoIsomorphicSubstrings(s):
    len_each_case = list()
    learned_pattern = list()
    for cur_index in range(1, len(s)+1):
        splited_str = s[:cur_index]
        for read_length in reversed(range(cur_index)):
            char = splited_str[read_length:cur_index]
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

        yield len(learned_pattern)


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

