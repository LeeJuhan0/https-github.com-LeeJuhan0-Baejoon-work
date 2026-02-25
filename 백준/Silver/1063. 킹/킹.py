k, s, n = input().split()
move = list(input() for _ in range(int(n)))
grid = [[0 for _ in range(8)]for _ in range(8)]
grid[8 - int(k[1])][ord(k[0])-ord('A')] = -1
grid[8 - int(s[1])][ord(s[0])-ord('A')] = 1

def in_range(x,y) :
    if 0 <= x and x < 8 and 0 <= y < 8 :
        return True
    return False
king_x = ord(k[0])-ord('A')
king_y = 8 - int(k[1])
stone_x = ord(s[0])-ord('A')
stone_y = 8 - int(s[1])

for m in move :
    if m == 'R':
        dx = 1
        dy = 0
    elif m == 'L' :
        dx = -1
        dy = 0
    elif m == 'B' :
        dx = 0
        dy = 1
    elif m == 'T' :
        dx = 0
        dy = -1
    elif m == 'RT' :
        dx = 1
        dy = -1
    elif m == 'LT' :
        dx = -1
        dy = -1
    elif m == 'RB' :
        dx = 1
        dy = 1
    elif m == 'LB' :
        dx = -1
        dy = 1
    next_x = king_x + dx
    next_y = king_y + dy
    snext_x = stone_x + dx
    snext_y = stone_y + dy
    if in_range(next_x, next_y) and grid[next_y][next_x] != 1:
        grid[king_y][king_x] = 0
        grid[next_y][next_x] = -1
        king_x, king_y = next_x, next_y
    elif in_range(next_x, next_y) and grid[next_y][next_x] == 1 :
        if in_range(snext_x, snext_y) :
            grid[king_y][king_x] = 0
            grid[next_y][next_x] = -1
            grid[snext_y][snext_x] = 1
            king_x, king_y = next_x, next_y
            stone_x, stone_y = snext_x, snext_y
        else :
            continue
    else :
        continue

stone = ''
king = ''
for r in range(8):
    for c in range(8) :
        if grid[r][c] == 1:
            stone += chr(c + int(ord('A')))
            stone += str(8 - r)
        if grid[r][c] == -1:
            king += chr(c + int(ord('A')))
            king += str(8 - r)
            
print(king,"\n" + stone)
