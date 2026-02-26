def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1] = 0, 1
    for i in range(n-1):
        dp[i+2] = dp[i] + dp[i+1]
    return dp[-1]%1234567