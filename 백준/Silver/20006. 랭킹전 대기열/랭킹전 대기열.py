import math
p, m = map(int, input().split())
player_level = []
player_name = []

for i in range(p):
    a, b = input().split()
    
    player_level.append(int(a))
    player_name.append(b)

def matching(player_level, player_name, m):
    if len(player_level) == 0 :
        return 0;
    idx = 0
    cnt = 0
    start_flag = True
    room = []
    while cnt < m :
        if len(player_level) <= idx:
            break;
        if start_flag : 
            first_level = player_level[0]
            cnt += 1
            room.append([player_level[0], player_name[0]])
            player_level = player_level[1:]
            player_name = player_name[1:]
            start_flag = False
            if len(player_level) == 0 :
                break
            if cnt >= m :
                break
           
        if level(first_level,player_level[idx]) :
            room.append([player_level[idx], player_name[idx]])
            player_level = player_level[:idx] + player_level[idx+1:]
            player_name = player_name[:idx] + player_name[idx+1:]
            cnt += 1
        else :
            idx += 1
    room = sorted(room, key=lambda x: x[1])
    if len(room) == m :
        print('Started!')
        for i in room :
            print(f'{i[0]} {i[1]}')
    else :
        print('Waiting!')
        for i in room :
            print(f'{i[0]} {i[1]}')
    return matching(player_level, player_name, m)


def level(a,b):
    if abs(a-b) <= 10 :
        return True
    else:
        return False

matching(player_level, player_name, m)
    