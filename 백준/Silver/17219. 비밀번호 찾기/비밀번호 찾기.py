n, m = map(int, input().split())
addresses = {}
for i in range(n):
    k, v = map(str, input().split())
    addresses[k] = v

for i in range(m):
    target = input()
    print(addresses[target])