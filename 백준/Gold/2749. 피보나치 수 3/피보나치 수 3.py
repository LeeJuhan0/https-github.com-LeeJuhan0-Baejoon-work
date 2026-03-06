import sys

MOD = 1_000_000
PISANO = 1500000  

n = int(sys.stdin.readline())
n %= PISANO

a, b = 0, 1  
for _ in range(n):
    a, b = b, (a + b) % MOD

print(a)