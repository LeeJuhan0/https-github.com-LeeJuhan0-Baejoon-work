from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    pointer = location 
    for i in priorities :
        q.append(i)
    check = True
    qm = max(q)
    while check :
        if q[0] < qm :
            q.append(q.popleft()) # 9 1 1 1 1 1 pointer 4, 1 1 1 1 1 pointer 3
            if pointer > 0:
                pointer -= 1
            else :
                pointer = len(q)-1
        else :
            q.popleft()
            answer += 1
            if pointer == 0 :
                return answer   
            qm = max(q)
            pointer -= 1

    return answer 
