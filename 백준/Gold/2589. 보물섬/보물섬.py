from collections import deque

n, m = map(int, input().split())
treasure = []
for i in range(n):
    row = str(input())
    pashing_row = list(row)
    treasure.append(pashing_row)

def treasure_island(q,r,c):
    s = q.popleft()
    if s == 'W' :
        return 0
    dist = [[-1]*m for _ in range(n)]
    dist[r][c] = 0
    q2 = deque()
    q2.append([treasure[r][c], r, c])
    while q2:
        s = q2.popleft()
        if s[0] == 'W' :
            continue
        else :
            left = s[2] - 1
            if  left >= 0 and treasure[s[1]][left] == 'L' and dist[s[1]][left] == -1 :
                dist[s[1]][left] = dist[s[1]][s[2]] + 1
                q2.append([treasure[s[1]][left], s[1], left])

            right = s[2] + 1
            if right < m and treasure[s[1]][right] == 'L' and dist[s[1]][right] == -1:
                dist[s[1]][right] = dist[s[1]][s[2]] + 1
                q2.append([treasure[s[1]][right], s[1], right])
            
            down = s[1]+1
            if down < n and treasure[down][s[2]] == 'L' and dist[down][s[2]] == -1:
                dist[down][s[2]] = dist[s[1]][s[2]] + 1
                q2.append([treasure[down][s[2]], down, s[2]])
                
            up = s[1]-1
            if up >= 0 and treasure[up][s[2]] == 'L' and dist[up][s[2]] == -1:
                dist[up][s[2]] = dist[s[1]][s[2]] + 1
                q2.append([treasure[up][s[2]], up, s[2]])
    return max(map(max, dist))

result = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        q = deque()
        q.append(treasure[i][j])
        result[i][j] = treasure_island(q,i,j)

print(max(map(max, result)))



    





            
        
        