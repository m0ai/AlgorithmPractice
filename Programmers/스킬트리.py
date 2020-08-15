# https://programmers.co.kr/learn/courses/30/lessons/49993
from typing import List
import unittest


def is_valid_skill_tree(valid_skill: str, user_skill_tree: str) -> bool:
    return valid_skill.startswith(''.join(list(dict.fromkeys(filter(lambda x: x in valid_skill, user_skill_tree)))))


def solution(skill:str , skill_trees: List[str]) -> int:
    return sum([is_valid_skill_tree(skill, skill_tree) for skill_tree in skill_trees])


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2, solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"],))


if __name__ == '__main__':
    unittest.main()

