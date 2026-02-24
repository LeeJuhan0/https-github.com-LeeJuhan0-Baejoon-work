x, y = map(int, input().split())
n = int(input())

def get_1d_distance(dir, dist):
    if dir == 1:   # 북
        return dist
    elif dir == 4: # 동
        return x + dist
    elif dir == 2: # 남
        return x + y + (x - dist)
    elif dir == 3: # 서
        return x + y + x + (y - dist)

shops = []
for _ in range(n):
    d, dist = map(int, input().split())
    shops.append(get_1d_distance(d, dist))

loc_d, loc_dist = map(int, input().split())
guard = get_1d_distance(loc_d, loc_dist)

total_perimeter = 2 * (x + y)
answer = 0

for shop in shops:
    dist1 = abs(guard - shop)
    dist2 = total_perimeter - dist1
    answer += min(dist1, dist2)

print(answer)