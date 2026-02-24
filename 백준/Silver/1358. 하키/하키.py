w, h, x, y, p = map(int, input().split())
loc = [list(map(int, input().split())) for _ in range(p)]
r = int(h/2)

def in_range(c_x,c_y) :
    if c_x >= x and c_x <= x + w and c_y >= y and c_y <= y + h :
        return True
    if ((c_x - x)**2+(c_y - (y+r))**2)**0.5 <= r:
        return True
    if ((c_x - (x+w))**2+(c_y - (y+r))**2)**0.5 <= r:
        return True
    return False

cnt = 0
for p in loc:
    if in_range(p[0], p[1]) :
        cnt += 1
print(cnt)