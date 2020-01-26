//실패 - 런타임 오류
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
            
//성공 - 리스트의 최솟값을 이용하는 문제이므로 heapq을 이용하였다.
import heapq

def solution(scoville,K):
    answer = 0
    scoville_heap = []
    for i in scoville:  //힙에 scoville의 모든 요소 넣기
        heapq.heappush(scoville_heap,i)
    while(1):
        if scoville_heap[0]>=K:
            return answer
        elif len(scoville_heap)==1:
            return -1
        else:
            Min = heapq.heappop(scoville_heap)
            Min2 = heapq.heappop(scoville_heap)
            heapq.heappush(scoville_heap, Min+Min2*2)
            answer += 1
