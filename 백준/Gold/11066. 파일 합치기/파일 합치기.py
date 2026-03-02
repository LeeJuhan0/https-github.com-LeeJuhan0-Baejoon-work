import sys
input = sys.stdin.readline
 
def solve():
 
    K = int(input())
    files = tuple(map(int, input().split()))
 
    S = [0] * (K+1)
    for i in range(K):
        S[i+1] = S[i] + files[i]
 
    dp = [[0]*K for _ in range(K)]
    kp = [[0]*K for _ in range(K)]
 
    for i in range(K - 1):
        kp[i][i+1] = i
        dp[i][i+1] = files[i] + files[i+1]

    for length in range(3, K + 1):
        for i in range(K - length + 1):
            j = i + length - 1
 
            best_k = 0
            min_cost = float('inf')
 
            start_k = kp[i][j-1]
            end_k = kp[i+1][j]
 
            for k in range(start_k, end_k + 1):
                best_cost = dp[i][k] + dp[k+1][j]
 
                if best_cost < min_cost:
                    best_k = k
                    min_cost = best_cost
 
            dp[i][j] = min_cost + (S[j + 1] - S[i])
            kp[i][j] = best_k
 
    print(dp[0][K-1])
 
T = int(input())
for _ in range(T):
    solve()