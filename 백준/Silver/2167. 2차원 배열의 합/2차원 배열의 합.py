import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
k = int(input().strip())
for _ in range(k) :
    i, j, x, y = map(int, input().split())
    sums = sum(list(sum(grid[p][j-1:y]) for p in range(i-1 , x)))
    print(sums)
    