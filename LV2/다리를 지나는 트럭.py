def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting = truck_weights
    length_truck = len(truck_weights)
    crossed = []   
    going = []
    on_the_bridge = []  

    while len(crossed) != length_truck:
        for i in range(len(going)): 
            going[i] += - 1
        if going and going[0] == 0:
            del going[0] 
            crossed.append(on_the_bridge.pop(0))  
        if waiting and weight >= sum(on_the_bridge) + waiting[0]: 
            on_the_bridge.append(waiting.pop(0))
            going.append(bridge_length)  
            print(going)
        answer += 1
    return answer
