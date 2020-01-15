def solution(heights):
    answer = []
    while len(heights) > 0:
        right = heights.pop()
        s = [i for i in heights]
        for i in range(len(s)):
            if right < s.pop():
                answer.append(len(s)+1)  #s스택에서 pop되었으므로 개수+1해준다.
                break
            elif len(s) == 0: 
                answer.append(0)  #맨 마지막 탑은 수신되는 탑이 없으므로 0추가
    answer.append(0)
    answer.reverse()
    return answer
