def solution(triangle):
    answer = 0
    for i in triangle :
        for j in range(len(triangle),0,-1):
            i.append(0)
    dp =[[0 for _ in range(len(triangle))] for _ in range(len(triangle))] 
    dp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)) :
        for j in range(0,len(triangle)) :
            if j == 0 :
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            else  :
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
    return max(dp[len(dp)-1])