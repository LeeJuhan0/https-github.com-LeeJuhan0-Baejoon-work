board = str(input())
chars = []
for char in board:
    chars.append(char)
cnt = 0 
possible = True
for i in range(len(chars)):
    if chars[i] == 'X' :
        cnt += 1
        try :
            if chars[i+1] == '.':
                if cnt % 2 == 1 :
                    possible = False
                    break
                else :
                    if cnt % 4 == 0 :
                        for j in range(cnt):
                            chars[i-j] = 'A'
                    else :
                        for j in range(cnt):
                            if j == 0 or j == 1 :
                                chars[i-j] = 'B'
                            else:
                                chars[i-j] = 'A'
        except :
            if cnt % 2 == 1 :
                    possible = False
                    break
            else :
                if cnt % 4 == 0 :
                    for j in range(cnt):
                        chars[i-j] = 'A'
                else :
                    for j in range(cnt):
                        if j == 0 or j == 1 :
                            chars[i-j] = 'B'
                        else:
                            chars[i-j] = 'A'
    else:
        cnt = 0
answer=''
for i in chars :
    answer += i
print(answer if possible else -1)

        