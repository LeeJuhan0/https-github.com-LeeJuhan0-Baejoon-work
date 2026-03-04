def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    for i in s:
        try :
            ex = int(i) + 1
        except :
            answer = False
    return answer