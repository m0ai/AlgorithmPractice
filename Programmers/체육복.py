from typing import List

def can_i_borrow_your_uniform(lost: int, reserve: List[int]) -> bool:
    if lost-1 in reserve:
        reserve.remove(lost-1)
        return True
    elif lost+1 in reserve:
        reserve.remove(lost+1)
        return True

    return False


def solution(n, lost, reserve):
    answer = n - len(lost)

    for l in sorted(lost):
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
            answer += 1

    for l in sorted(lost):
        if l-1 in reserve:
            answer += 1
            reserve.remove(l-1)
        elif l+1 in reserve:
            answer += 1
            reserve.remove(l+1)

    return answer


print(
    solution(5, [2,4], [1,3,5]) == 5
)

print(
    solution(5, [2,4], [3]) == 4
)

print(
    solution(3, [3], [1]) == 2
)

print(
    solution(5, [2,4], [1,3,5]) == 5
)

print(
    solution(5, [2,4], [3]) == 4
)

print(
    solution(5, [2,3,4], [1,2,4,5]) == 4
)

print(
    solution(5, [2,3], [3,4]) == 4
)

