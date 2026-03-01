n = int(input())
c = list(map(int, input().split()))
v = list(map(int, input().split()))

dp =[0 for _ in range(100)]

for i in range(n):
    value = v[i]
    cost = c[i]
    for health in range(99,-1,-1):
        if health < cost :
            continue
        dp[health] = max(dp[health], dp[health - cost] + value)
print(dp[-1])