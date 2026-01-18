import sys

n = int(sys.stdin.readline())
q = []
for i in range(n):
    a = sys.stdin.readline().strip()
    if a[:4] == 'push' :
        b, k = map(str, a.split())
        q.append(k)
    elif a == 'top' :
        print(q[-1]) if len(q) != 0 else print(-1)
    elif a == 'size' :
        print(len(q))
    elif a == 'empty' :
        print(1) if len(q) == 0 else print(0)
    elif a == 'pop' :
        print(q.pop()) if len(q) != 0 else print(-1)