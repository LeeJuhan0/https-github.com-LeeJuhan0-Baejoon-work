import sys
sys.setrecursionlimit(3000)
def solution(numbers, target):
    answer = 0
    def dfs(idx, curr_sum):
        nonlocal answer
        if idx == len(numbers):
            if curr_sum == target:
                answer += 1
            return
        dfs(idx + 1, curr_sum + numbers[idx])
        dfs(idx + 1, curr_sum - numbers[idx])
        
    dfs(0,0)
    return answer