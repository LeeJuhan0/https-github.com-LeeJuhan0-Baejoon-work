def solution(name, yearning, photo):
    answer = []
    names = []
    n = len(name)
    for i in range(len(name)) :
        names.append([name[i], yearning[i]])
    names.sort(key = lambda x:x[0])
    for persons in photo :
        persons.sort(reverse = True)
        score = 0
        while True:
            person = persons.pop()
            for i in range(n):
                if person == names[i][0] :
                    score += names[i][1] 
            if len(persons) == 0 :
                break
        answer.append(score)
            
    return answer