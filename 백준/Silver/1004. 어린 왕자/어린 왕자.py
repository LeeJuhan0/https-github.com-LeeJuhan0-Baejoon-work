n = int(input())
for _ in range(n) :
    start_x, start_y, end_x, end_y = map(int, input().split())
    m = int(input())
    answer = 0
    for _ in range(m) :
        cnt = 0
        x, y, r = map(int, input().split())
        if ((x-start_x)**2 + (y-start_y)**2)**0.5 < r :
            cnt += 1
        if ((x-end_x)**2 + (y-end_y)**2)**0.5 < r :
            cnt += 1
        if cnt == 1:
            answer+=1
    print(answer)
    