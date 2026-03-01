import sys
import heapq

input = sys.stdin.readline
INF = float('inf') #무한대 
n = int(input()) # 도시 개수(vertax)
m = int(input())#버스 개수(edge)

graph = [[] for _ in range(n+1)] 
#연결 상태와 비용 저장용 인접리스트 graph[u](출발 노드)에는 (w, v) (비용, 도착)의 형태의 연결지점만 포함

for _ in range(m):
    u, v, w = map(int, input().split())
    #출발, 도착, 비용
    graph[u].append((w, v))

start, end = map(int, input().split()) # 최초 출발점, 최종 도착점

def dijkstra(start):
    distances = [INF] * (n+1) #각 지점마다 도착했을 때 최소비용 distances[i] = i번째 도시에 도착하기 위한 최소 비용
    distances[start] = 0 # 출발지점의 최소도착비용은 0
    pq = [] #우선순위 큐 (누적 비용, 현재 위치(노드))
    heapq.heappush(pq, (0, start)) #시작점 넣기
    while pq:
        current_cost, current_node = heapq.heappop(pq) # 현재 비용과 위치 : pq에서 가장 작은 비용(x[0]가 기준이므로 w,v 형태로 넣는 이유)이 현재
        if distances[current_node] < current_cost: #현재 코스트가 원래 코스트보다 크면 갱신 불필요
            continue
        for weight, next_node in graph[current_node]: #현재 노드와 인접한 다음 노드와 비용 순회
            cost = current_cost + weight # 전체 코스트는 현재까지의 최소비용(다음에 최소값을 cost로 갱신해서 넣기 때문) + 다음 길의 비용
            if cost < distances[next_node] : # 코스트가 최소비용보다 작으면 갱신
                distances[next_node] = cost #최소비용을 현재 코스트로 갱신
                heapq.heappush(pq, (cost, next_node)) # 현재와 연결되어있고 & 현재 + 그 길의 비용 = 최소비용일 때만 다음 큐에 진입
    return distances
dist_table = dijkstra(start)
print(dist_table[end])