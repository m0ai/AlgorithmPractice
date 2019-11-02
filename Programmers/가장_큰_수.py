from functools import cmp_to_key

def altered_max(x: int, y: int):
    xy_concat_int = str(x) + str(y)
    yx_concat_int = str(y) + str(x)
    if xy_concat_int == max(xy_concat_int, yx_concat_int):
        return 1
    else:
        return -1

def solution(numbers):
    numbers.sort(key=cmp_to_key(altered_max), reverse=True)
    if max(numbers) == 0:
        return '0'

    return ''.join(map(str, numbers))

