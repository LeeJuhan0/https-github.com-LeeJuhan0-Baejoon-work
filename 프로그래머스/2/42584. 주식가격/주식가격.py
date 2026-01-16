from collections import deque

def solution(prices):
    answer = []
    price = deque(prices)
    chart = deque()
    while price :
        chart.append(price.popleft())
        time = 0
        for i in price:
            time += 1
            if chart[-1] <= i :
                continue
            else :
                break
        answer.append(time)
                
            
    return answer