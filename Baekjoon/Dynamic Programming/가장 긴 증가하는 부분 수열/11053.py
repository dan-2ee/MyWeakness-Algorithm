import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):   # 기준값 
    for j in range(i):   # 비교값
        if (nums[j] < nums[i]):
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))