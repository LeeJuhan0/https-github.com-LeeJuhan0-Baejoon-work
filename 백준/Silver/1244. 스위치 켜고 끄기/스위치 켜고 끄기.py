n = int(input())
switch = list(map(int, input().split()))
o_n = int(input())
orders = [list(map(int, input().split())) for _ in range(o_n)]

for order in orders :
    if order[0] == 1:
        for j in range(1, n // order[1] + 2):
            try :
                switch[order[1] * j -1] = (switch[order[1] * j -1] + 1) % 2
            except :
                break
    elif order[0] == 2 :
        switch[order[1] - 1] = (switch[order[1] -1] + 1) % 2
        cnt = 0
        flag = True
        while flag :
            cnt += 1
            try :
                if switch[order[1] - 1 + cnt] == switch[order[1] - 1 -cnt] and order[1] - 1 - cnt >= 0 :
                    switch[order[1] -1 + cnt] = (switch[order[1] - 1 + cnt] + 1) % 2
                    switch[order[1] -1 - cnt] = (switch[order[1] - 1 - cnt] + 1) % 2
                else :
                    flag = False
            except : 
                flag = False
        
for i in range(1,len(switch) // 20 + 2) :
    print(*switch[20*(i-1):20*i])

