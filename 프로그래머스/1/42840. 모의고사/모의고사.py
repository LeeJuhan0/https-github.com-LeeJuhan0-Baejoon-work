
def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0,0,0]
    for i in range(len(answers)) :
        check = answers[i]
        f = first[i%len(first)]
        if  f == check :
            scores[0] += 1
        s = second[i%len(second)]
        if s == check :
            scores[1] += 1
        t = third[i%len(third)]
        if t == check :
            scores[2] += 1
    result = []
    val = max(scores)
    for i in range(3) :
        if val == scores[i] :
            result.append(i+1)
    
    return result