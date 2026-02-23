from collections import deque
n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()
q = deque(rope)

max_weigh = -1
while(q):
    min_weigh = q.popleft()
    if max_weigh < (len(q)+1) * min_weigh :
        max_weigh = (len(q)+1) * min_weigh

print(max_weigh)

