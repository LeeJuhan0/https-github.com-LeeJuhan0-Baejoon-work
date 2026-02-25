import sys
input = sys.stdin.readline
n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort(reverse = True)
flag = False
cnt = 0
i = 0
while True :
    if flag:
        break
    idx = 1
    while True :
        if i + idx == n :
                cnt += 1
                flag = True
                break
        if hole[i] - hole[i+idx] + 1 <= l :
            idx += 1
            continue
        else :
            cnt += 1
            i = i + idx
            break
            
print(cnt)