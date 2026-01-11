n = int(input())
arr = list(map(int, input().split()))

intMax= 10**9
dp = [intMax]*n
dp[0] = 0
for i in range(n) :
    if dp[i] == intMax:
        continue
    step = arr[i]
    for j in range(i+1, min(i+step+1,n)):
        dp[j] = min(dp[j], dp[i] + 1)

print(-1 if dp[n-1] == intMax else dp[n-1])