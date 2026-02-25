n = int(input())
sqs = list(list(map(int, input().split())) for _ in range(n))
grid = [[0 for _ in range(102)] for _ in range(102)]
for sq in sqs:
    for y in range(sq[1]+1,sq[1]+11):
        for x in range(sq[0]+1,sq[0]+11):
            grid[y][x] = 1
sum = 0
for y in range(102):
        for x in range(102):
            if grid[y][x] == 0 :
                continue
            dxs, dys = [0,1,0,-1], [1,0,-1,0]
            cnt = 0
            for dx, dy in zip(dxs, dys) :
                next_x, next_y = x + dx, y + dy
                if grid[next_y][next_x] == 0 :
                    cnt += 1
            if cnt != 0 :
                sum += cnt
                
print(sum)