def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i] :
            dfs(i, visited, n, computers)
            answer += 1
    return answer

def dfs(vertax, visited, n, computers) :
    visited[vertax] = True
    curr_t = vertax
    for i in range(n) :
        if not visited[i] and computers[vertax][i] == 1 :
            dfs(i, visited, n, computers)