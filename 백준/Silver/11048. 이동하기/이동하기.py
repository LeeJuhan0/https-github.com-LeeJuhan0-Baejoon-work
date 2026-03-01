import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = []
for i in range(n) :
    grid.append(list(map(int, input().split())))

dp = [[0 for _ in range(m)] for _ in range(n)]

for r in range(n):
    for c in range(m):
        if r == 0 and c == 0 :
            dp[r][c] = grid[r][c]
        elif r == 0 :
            dp[r][c] = grid[r][c] + dp[r][c-1]
        elif c == 0 :
            dp[r][c] = grid[r][c] + dp[r-1][c]
        else :
            dp[r][c] = grid[r][c] + max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

print(dp[n-1][m-1])
        