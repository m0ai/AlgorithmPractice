


'''

Single = 1
Double = 2
Triple = 3



* 은 이전 점수 *2 + 현재점수  *2

# 현재점수를 총점에서 마이너스
'''

import re

def solution(dart_result):
    score_board = list()
    p = re.compile('([0-9]+)([S|D|T])([#|*])?')
    bonus_macth_table  = {'S' : 1, 'D' : 2, 'T' : 3}
    for m in p.finditer(dart_result):
        score, bonus, optional = m.groups()
        score = int(score)** bonus_macth_table[bonus]
        if optional == '*':
            if len(score_board) > 0:
                score_board.append(score_board.pop()*2)
            score *= 2
        elif optional == '#':
            score *= -1
        score_board.append(score)
    return sum(score_board)

print(solution('1S2D*3T'))





