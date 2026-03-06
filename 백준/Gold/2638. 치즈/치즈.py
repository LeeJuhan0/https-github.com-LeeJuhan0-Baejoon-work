from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
new_grid = [[0 for _ in range(m)] for _ in range(n)] 
visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    dq = deque([(x, y)])
    visited[x][y] = True
    grid[x][y] = -1
    while dq:
        x, y = dq.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and (not visited[nx][ny]) and grid[nx][ny] == 0:
                visited[nx][ny] = True
                grid[nx][ny] = -1
                dq.append((nx, ny))

def find_melt(x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == -1:
            cnt += 1
    return cnt >= 2

time = 0
while any(1 in row for row in grid):
    time += 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == -1:
                grid[i][j] = 0

    visited = [[False for _ in range(m)] for _ in range(n)]

    if grid[0][0] == 0:
        bfs(0, 0)
    else:
        pass

    new_grid = [row[:] for row in grid]

    for x in range(1, n - 1):
        for y in range(1, m - 1):
            if grid[x][y] == 1:
                if find_melt(x, y):
                    new_grid[x][y] = 0
                else:
                    new_grid[x][y] = 1

    grid = new_grid

print(time)