def solution(brown, yellow):
    num = brown + yellow
    num_list = []
    answer = []
    for i in range(2,int(num**0.5)+1):
        if num % i == 0 :
            num_list.append([int(num/i),i])
    print(num_list)
    for i in num_list :
        if (i[0]-2) * (i[1]-2) == yellow and i[0] >= i[1] :
            answer.append(i)
    print(answer)  
    return answer[0]