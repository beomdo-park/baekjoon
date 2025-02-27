import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

dp = [nums[0]] + [0 for i in range(n - 1)]

for i in range(1, n):
    if dp[i - 1] < 0:
        dp[i] = nums[i]
    else:
        dp[i] = nums[i] + dp[i - 1]
print(max(dp))
