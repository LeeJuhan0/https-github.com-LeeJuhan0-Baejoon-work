import sys
input = sys.stdin.readline
n = int(input().strip())
tops = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(n)]
for i in range(n):
    while stack and stack[-1][1] < tops[i]:
        stack.pop()
    
    if stack:
        answer[i] = stack[-1][0] + 1  
        
    stack.append((i, tops[i]))
print(*answer)
    