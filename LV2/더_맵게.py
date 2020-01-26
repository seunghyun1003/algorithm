//시도1. 실패 - 런타임 오류
def scoville_min(scoville_list):
    MIN = min(scoville_list)
    return scoville_list.pop(MIN)

def solution(scoville, K):
    answer = 1
    for i in range(len(scoville)):
        if scoville[i] < K:
            answer += 1
            x = scoville_min(scoville)
            x2 = scoville_min(scoville)
            scoville.append(x + x2*2)
        else:
            return answer
            
//
