#!/bin/python

from __future__ import print_function

import os
import sys
def pseudoIsomorphicSubstrings(s):
    len_each_case = list()
    learned_patterns = list()
    for cur_index in range(1, len(s)+1):
        splited_str = s[:cur_index]
        for read_length in reversed(range(cur_index)):
            element_num = 0
            char = splited_str[read_length:cur_index]
            new_pattern = list()
            pattern_match_dict = {}

            for c in char:
                if c not in pattern_match_dict:
                    pattern_match_dict[c] =element_num
                    new_pattern += 1
                new_pattern.append(pattern_match_dict[c])

            if new_pattern not in learned_patterns:
                learned_patterns.append(new_pattern)

        yield len(learned_patterns)


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

