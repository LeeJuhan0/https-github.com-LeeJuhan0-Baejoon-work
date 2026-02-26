import sys
input = sys.stdin.readline
n = int(input().strip())
nums = list(map(int, input().split()))
nums.sort()
answer = 0

for i in range(n):
    target = nums[i]
    left = 0
    right = n - 1
    while left < right :
        if left == i :
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        sum_val = nums[left] + nums[right]

        if sum_val == target:
            answer += 1
            break
        elif sum_val < target:
            left += 1
        else :
            right -= 1
print(answer)
