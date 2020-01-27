from heapq import heappush, heappop

def solution(stock, dates, supplies, k):
    count = 0
    heap = []
    for i in range(len(dates)):
        if dates[i] > k:
            dates.remove(i)
            supplies.remove(i)
    dates.pop(0)
    dates.append(k)
    
    for i, supply_dates in enumerate(dates):
        heappush(heap, -1*supplies[i])  #supplies의 최대값 출력. heapq은 최소힙만을 지원하므로 supplies을 음수로 만들어 최대값을 출력한다.
        while (stock < supply_dates):
            max_supplies = -1*heappop(heap)
            stock += max_supplies
            count += 1
            if max_supplies == 0:
                break
    return count
