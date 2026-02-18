n, m = map(int, input().split())
nums = list(map(int, input().split()))
d = {}
answer = []

for i in nums :
    try:
        d[i] += 1
    except:
        d[i] = 1

while len(d) != 0 :
    for _ in range(d[max(d, key=d.get)]):
        answer.append(max(d, key=d.get))
    del d[max(d, key=d.get)]

print(*answer)
        
    