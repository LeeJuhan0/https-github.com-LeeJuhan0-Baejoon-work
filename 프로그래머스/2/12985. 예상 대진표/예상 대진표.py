def solution(n,a,b):
    answer = 0

    while True :
        if abs(a - b) == 0:
            break
        a, b = int(a/2 + 0.5) , int(b/2 + 0.5)
        answer += 1
        
    return answer