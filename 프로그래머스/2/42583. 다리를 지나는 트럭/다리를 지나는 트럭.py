from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length) 
    trucks = deque(truck_weights)
    total_weight = 0
    while bridge :
        answer += 1
        total_weight -= bridge.popleft()
        if trucks:
            if total_weight + trucks[0] <= weight : #진입
                bridge.append(trucks.popleft())
                total_weight += bridge[-1]
            else :
                bridge.append(0)
    
    return answer
