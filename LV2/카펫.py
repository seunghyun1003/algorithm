def solution(brown, red):
    for i in range(1, red//2+1): #red가 1일경우 red//2는 0이 되므로 +1해준다.
        if red % i == 0:
            if brown == (i+red//i+2)*2:
                return [red//i+2, i+2]
