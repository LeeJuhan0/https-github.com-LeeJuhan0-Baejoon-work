import sys
min_value = -sys.maxsize 
n, l_t = map(int, input().split())
v = [0]
t = [0]
for _ in range(n):
    time, value = map(int, input().split())
    v.append(value)
    t.append(time)
dp = [[min_value for _ in range(l_t+1)] for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1) :
    time = t[i]
    value = v[i]
    for limit in range(l_t,-1,-1):
        if  time <= limit :
            dp[i][limit] = max(dp[i-1][limit], dp[i-1][limit-time] + value)
        else :
            dp[i][limit] = dp[i-1][limit]

print(max(dp[n]))