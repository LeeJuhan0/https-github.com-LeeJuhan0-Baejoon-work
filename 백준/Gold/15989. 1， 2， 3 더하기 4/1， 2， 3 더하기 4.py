n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
maximum = max(num_list)
dp = [1] * 10001

for i in range(2, maximum+1):
    dp[i] += dp[i-2]
for i in range(3, maximum+1):
    dp[i] += dp[i-3]

for i in num_list:
    print(dp[i])