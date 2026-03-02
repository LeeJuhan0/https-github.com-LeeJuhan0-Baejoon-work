n = int(input())
nums = list(map(int, input().split()))

dp_left = [1 for _ in range(n)]
dp_right  = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if nums[j] < nums[i] :
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)

max_v = 0
for i in range(n):
    max_v = max(max_v, dp_left[i] + dp_right[i] - 1)
print(max_v)
