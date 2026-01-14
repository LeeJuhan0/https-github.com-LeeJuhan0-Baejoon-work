def solution(s):
    answer = True
    open = 0
    close = 0
    for i in s :
        if i == '(' :
            open += 1
        elif i == ')' :
            close += 1
        if open < close :
            return False
    
    return True if open == close else False