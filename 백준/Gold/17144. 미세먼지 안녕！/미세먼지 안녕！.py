n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(m)] for _ in range(n)]
def flow(grid, next_grid):
    for x in range(n):
        for y in range(m):
            if grid[x][y] == -1 :
                next_grid[x][y] = -1
                continue
            if grid[x][y] < 5:
                next_grid[x][y] += grid[x][y]
                continue
            dxs, dys = [-1,1,0,0], [0,0,1,-1]
            cnt = 0
            for dx, dy in zip(dxs, dys):
                next_x = x + dx
                next_y = y +dy
                if can_go(next_x, next_y, grid):
                    cnt += 1
                    next_grid[next_x][next_y] += grid[x][y]//5
            next_grid[x][y] += grid[x][y] - (grid[x][y]//5) * cnt

    return next_grid

def in_range(x,y):
    if 0 <= x < n and 0 <= y < m :
        return True
    return False

def can_go(x,y,grid) :
    if not in_range(x,y) :
        return False
    if grid[x][y] == -1 :
        return False
    return True
    
def wind(grid, up, down):
    up_x, up_y = up[0]-1, up[1]
    up_dxs, up_dys = [-1,0,1,0], [0,1,0,-1]
    indicator = 0
    while True :
        next_up_x = up_x + up_dxs[indicator]
        next_up_y = up_y + up_dys[indicator]
        if not in_range(next_up_x, next_up_y) or (indicator == 2 and next_up_x == up[0] + 1) :
            indicator = (indicator + 1)
            next_up_x = up_x + up_dxs[indicator]
            next_up_y = up_y + up_dys[indicator]
        if grid[next_up_x][next_up_y] == -1 :
            grid[up_x][up_y] = 0
            break
        grid[up_x][up_y] = grid[next_up_x][next_up_y]
        up_x, up_y = next_up_x, next_up_y

    down_x, down_y = down[0] + 1, down[1]
    down_dxs, down_dys = [1,0,-1,0], [0,1,0,-1]
    indicator = 0
    while True:
        next_down_x, next_down_y = down_x + down_dxs[indicator], down_y + down_dys[indicator]
        if not in_range(next_down_x, next_down_y) or (indicator == 2 and next_down_x == down[0] - 1):
            indicator = (indicator + 1)
            next_down_x, next_down_y = down_x + down_dxs[indicator], down_y + down_dys[indicator]
        if grid[next_down_x][next_down_y] == -1:
            grid[down_x][down_y] = 0
            break
        grid[down_x][down_y] = grid[next_down_x][next_down_y]
        down_x, down_y = next_down_x, next_down_y
          
    return grid

def clean_map(n, m, t, grid, next_grid):
    machine = []
    for x in range(n):
        for y in range(m):
            if grid[x][y] == -1 :
                machine.append([x,y])
    summ = 2
    for i in range(t):
        grid = flow(grid, next_grid)
        next_grid = [[0 for _ in range(m)] for _ in range(n)]
        grid = wind(grid, machine[0], machine[1])
    for i in grid :
        summ += sum(i)
    return summ


print(clean_map(n,m,t,grid, next_grid))