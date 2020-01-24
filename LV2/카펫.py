def solution(brown, red):
    answer = [red+2, 3]
    for i in range(1, red//2):
        if red % i == 0:
            if brown == (i+red//i+2)*2:
                answer = [red//i+2, i+2]
    return answer
