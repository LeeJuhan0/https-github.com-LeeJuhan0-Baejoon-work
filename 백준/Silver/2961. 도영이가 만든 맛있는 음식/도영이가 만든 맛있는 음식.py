from itertools import combinations
n = int(input())
food=[]
for i in range(n):
    food.append(list(map(int, input().split())))
perm = []
for i in range(1,n+1):
    perm.append(list(combinations(food,i)))

diff = 2**31-1

for i in range(len(perm)) :
    for j in range(len(perm[i])) :
        sour=1
        salty=0
        for k in range(i+1):
            sour *= perm[i][j][k][0]
            salty += perm[i][j][k][1]
        if  abs(sour-salty) < diff :
            diff = abs(sour-salty)
print(diff)