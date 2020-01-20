def solution(clothes):
    answer = 1
    hash_table = dict()
    for name, kinds in clothes:
        hash_table[kinds] = hash_table.get(kinds, 0) + 1  #키가 없을 경우 0반환
        
    for v in hash_table.values():
        answer *= (v + 1)
    return answer-1
