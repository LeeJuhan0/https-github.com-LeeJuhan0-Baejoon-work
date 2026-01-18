from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
def cross_bridge(n, w, l, trucks) :
    bridge = deque([0 for _ in range(w)])
    time = 0
    start_trucks = deque(trucks)
    bridge_weight = 0
    while start_trucks:
        time += 1
        bridge_weight -= bridge[0]
        bridge.popleft()
        if bridge_weight + start_trucks[0] <= l :
            bridge.append(start_trucks.popleft())
            bridge_weight += bridge[-1]
        else :
            bridge.append(0)
    time += w
    return time
print(cross_bridge(n, w, l, trucks))