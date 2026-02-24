n, m, t = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
next_map = [[0 for _ in range(m)] for _ in range(n)]
def flow(map, next_map):
    for x in range(n):
        for y in range(m):
            if map[x][y] == -1 :
                next_map[x][y] = -1
                continue
            if map[x][y] < 5:
                next_map[x][y] += map[x][y]
                continue
            dxs, dys = [-1,1,0,0], [0,0,1,-1]
            cnt = 0
            for dx, dy in zip(dxs, dys):
                next_x = x + dx
                next_y = y +dy
                if can_go(next_x, next_y, map):
                    cnt += 1
                    next_map[next_x][next_y] += map[x][y]//5
            next_map[x][y] += map[x][y] - (map[x][y]//5) * cnt

    return next_map

def in_range(x,y):
    if 0 <= x < n and 0 <= y < m :
        return True
    return False

def can_go(x,y,map) :
    if not in_range(x,y) :
        return False
    if map[x][y] == -1 :
        return False
    return True
    
def wind(map, up, down):
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
        if map[next_up_x][next_up_y] == -1 :
            map[up_x][up_y] = 0
            break
        map[up_x][up_y] = map[next_up_x][next_up_y]
        up_x, up_y = next_up_x, next_up_y

    down_x, down_y = down[0] + 1, down[1]
    down_dxs, down_dys = [1,0,-1,0], [0,1,0,-1]
    indicator = 0
    while True:
        next_down_x, next_down_y = down_x + down_dxs[indicator], down_y + down_dys[indicator]
        if not in_range(next_down_x, next_down_y) or (indicator == 2 and next_down_x == down[0] - 1):
            indicator = (indicator + 1)
            next_down_x, next_down_y = down_x + down_dxs[indicator], down_y + down_dys[indicator]
        if map[next_down_x][next_down_y] == -1:
            map[down_x][down_y] = 0
            break
        map[down_x][down_y] = map[next_down_x][next_down_y]
        down_x, down_y = next_down_x, next_down_y
          
    return map

def clean_map(n, m, t, map, next_map):
    machine = []
    for x in range(n):
        for y in range(m):
            if map[x][y] == -1 :
                machine.append([x,y])
    summ = 2
    for i in range(t):
        map = flow(map, next_map)
        next_map = [[0 for _ in range(m)] for _ in range(n)]
        map = wind(map, machine[0], machine[1])
    for i in map :
        summ += sum(i)
    return summ


print(clean_map(n,m,t,map, next_map))