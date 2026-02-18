import copy
n = int(input())
have = {}
sum = 0

for i in range(n):
    values = list(map(str, input().split()))
    if values[0] == '1' : # 고릴라가 정보 얻은 상황
        name = values[1]
        values = copy.deepcopy(values[3:])
        values = list(map(int, values))
        try : # 이미 정보가 있던 상황
            for i in values:
                have[name].append(i)
        except : # 처음 고릴라 이름 들어온 상황
            have[name] = []
            for i in values:
                have[name].append(i)
    elif values[0] == '2' : # 호석이가 정보산 상황     
        name = values[1]
        want_cnt = values[2]
        try :
            have[name].sort()
            for _ in range(int(want_cnt)):
                sum += have[name].pop()
        except :
            pass
    

print(sum)
