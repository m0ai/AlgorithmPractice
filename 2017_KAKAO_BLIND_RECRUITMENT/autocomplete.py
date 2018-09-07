def solution(words):
    moai = dict()
    total = 0

    for i in range(1, len(max(words, key=len))+1):
        curr = dict()
        for k, word in enumerate(words.copy()):
            if not word[:i] in curr:
                curr[word[:i]] = {'count' : 1, 'words' : [word]}
            else:
                curr[word[:i]]['count'] += 1
                curr[word[:i]]['words'].append(word)
            if word[:i] == word:
                words.remove(word[:i])
            total += 1

        if len(curr) > 0:
            be_removed = [v['words'].pop() for d,v in curr.items() if v['count'] == 1]
            words = list(set(words) - set(be_removed))

    return total

curr_case= [['go','gone','guild'], ['abc','def','ghi','jklm'], ['word', 'war', 'warrior', 'world']]

for tc in curr_case:
    print(solution(tc))
