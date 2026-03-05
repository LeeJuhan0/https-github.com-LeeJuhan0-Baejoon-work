n = int(input())
words = list(input() for _ in range(n))
cnt = 0
for i in range(n):
    check = set()
    prev_ch = ''
    for ch in words[i] :
        if ch in check:
            break
        if ch == prev_ch :
            continue
        else :
            check.add(prev_ch)
        prev_ch = ch
    else :
        cnt +=1
        
print(cnt)