def solution(n, wires):
    cnt = 0
    w = [1] * n 

    adj = [[0] * n for _ in range(n)]

    for i, j in wires:
        adj[i-1][j-1] = 1
        adj[j-1][i-1] = 1
    print(adj)    
    while cnt < n-2: 
        leaves = []
        for i in range(n):
            if sum(adj[i]) == 1:
                leaves.append(i)

        for i in leaves:
            for j in range(n):
                if adj[i][j] == 1:
                    w[j] += w[i]
                    break 

        for i in leaves:
            for j in range(n):
                adj[i][j] = 0
                adj[j][i] = 0
        cnt += len(leaves)
        print(leaves)
    print(w)

    answer = 101
    for v in w:
        if abs(v - (n-v)) < answer:
            answer = abs(v - (n-v))

    return answer

