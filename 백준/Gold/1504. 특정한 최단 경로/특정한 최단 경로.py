from heapq import heappush, heappop
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(e) :
    s, e, d = map(int, input().split())
    graph[s].append((d, e))
    graph[e].append((d, s))

stopover1, stopover2 = map(int, input().split()) 

def dijkstra(start):
    min_dist = [float('inf') for _ in range(n+1)]
    min_dist[start] = 0
    pq = [(0, start)]
    while pq :
        curr = heappop(pq)
        curr_c, curr_n = curr[0], curr[1]
        if curr_c > min_dist[curr_n] :
            continue
        for next in graph[curr_n] :
            dist, next_n = next[0], next[1] 
            next_cost = dist + curr_c
            if next_cost < min_dist[next_n]:
                min_dist[next_n] = next_cost
                heappush(pq, (next_cost, next_n))

    return min_dist


answer = min(dijkstra(1)[stopover1] + dijkstra(stopover1)[stopover2] + dijkstra(stopover2)[n], dijkstra(1)[stopover2] + dijkstra(stopover2)[stopover1] + dijkstra(stopover1)[n])
print(answer if answer != float('inf') else -1)