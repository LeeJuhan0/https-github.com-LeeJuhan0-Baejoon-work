def solution(n, w, num):
    num -= 1
    n -= 1

    t_row = num // w
    if t_row % 2 == 0:
        t_col = num % w
    else:
        t_col = w - 1 - (num % w)
        
    answer = 0
    max_row = n // w  
    
    for r in range(t_row, max_row + 1):
        if r % 2 == 0:
            box_idx = r * w + t_col
        else:
            box_idx = r * w + (w - 1 - t_col)
            
        if box_idx <= n:
            answer += 1
            
    return answer