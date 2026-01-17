def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for x, y in puddles:
        dp[y-1][x-1] = -1


    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue

            if i == 0 and j == 0:
                continue
            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j-1] if j > 0 else 0
            
            dp[i][j] = (up + left) % 1000000007

    return dp[n-1][m-1]
