import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
sum = -1

while len(nums) >= 3 :
    if nums[-1] < nums[-2] + nums[-3] :
        sum += nums[-1] + nums[-2] + nums[-3] + 1
        break
    else :
        nums.pop()

print(sum)