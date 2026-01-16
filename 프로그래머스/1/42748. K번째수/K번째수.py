def solution(array, commands):
    answer = []
    for i in commands:
        cut = array[i[0]-1 : i[1]]
        cut.sort()
        answer.append(cut[i[2]-1])
    return answer