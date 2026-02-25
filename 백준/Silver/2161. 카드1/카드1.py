from collections import deque 
n = int(input())
q = deque()
for i in range(1,n+1):
    q.append(i)
answer = []
while q :
    waste = q.popleft()
    answer.append(waste)
    try:
        q.append(q.popleft())
    except:
        break
print(*answer)