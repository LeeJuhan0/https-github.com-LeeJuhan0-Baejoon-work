a, b = map(int, input().strip().split(' '))
row = ['*' for _ in range(a)]
for i in range(b):
    print(''.join(row))
