from collections import deque

F, S, G, U, D= map(int, input().split())
N = -1
dist = [-1] * (F+1)
q = deque()
dist[S] = 0
q.append(S) 

def startlink():
    while q:
        i = q.popleft()
        if i == G:
            print(dist[i])
            return
        
        N = i + U
        if U > 0 and N <= F and dist[N] == -1:
            dist[N] = dist[i] + 1
            q.append(N)
        
        N = i - D
        if D > 0 and N >= 1 and dist[N] == -1:
            dist[N] = dist[i] + 1
            q.append(N)
    print("use the stairs")
startlink()

