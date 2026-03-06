target , n = map(int, input().split())

coin = []
for i in range(0,21):
    coin.append(i)

dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
for i in range(target+1) :
    dp[1][i] += 1

for i in range(1,n+1):
    for j in range(target+1):
        if j == 0 :
            dp[i][j] = dp[i-1][j]
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1]%1000000000)