import sys
from heapq import heappop, heappush
INF = float('inf')
input = sys.stdin.readline
n, m, x  = map(int, input().split())

graph = [[] for _ in range(n+1)]
graph_r = [[] for _ in range(n+1)]

for  i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((c, e)) 
    graph_r[e].append((c, s))

def dijkstra(graph):
    distances = [INF for _ in range(n+1)]
    pq = [(0,x)]
    distances[x] = 0
    while pq :
        curr_cost, curr_v = heappop(pq)
        if curr_cost > distances[curr_v]:
            continue
        for cost, next_v in graph[curr_v] :
            next_cost = cost + curr_cost
            if distances[next_v] > next_cost :
                distances[next_v] = next_cost
                heappush(pq, (next_cost,next_v))
    return distances

dist = dijkstra(graph)
r_dist = dijkstra(graph_r)

max_v = 0
for i in range(1,n+1):
    total = dist[i] + r_dist[i]
    if max_v < total :
        max_v = total

print(max_v)