def solution(nums):
    answer = 0
    set_list = list(set(nums))
    if len(set_list) > len(nums)/2 :
        answer = len(nums)/2
    else :
        answer = len(set_list) 
        
    return answer