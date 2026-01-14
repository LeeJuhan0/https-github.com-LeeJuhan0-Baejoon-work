def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            answer = participant.pop(i)
            return answer
    if answer == '' :
        answer = participant[-1]
    return answer