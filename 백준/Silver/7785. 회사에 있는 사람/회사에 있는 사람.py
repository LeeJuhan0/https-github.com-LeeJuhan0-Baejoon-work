import sys
input = sys.stdin.readline
n = int(input().strip())
company = {}
for i in range(n):
    v, k = input().split()
    if k == 'enter':
        company[v] = 1
    else:
        del company[v]
company = list(company)
company.sort(reverse = True)
for p in company:
    print(p)