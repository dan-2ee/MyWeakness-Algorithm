import sys

input = sys.stdin.readline
N, M = list(map(int, input().strip().split()))
nums = [int(input()) for _ in range(N)]
nums.sort() 
result = sys.maxsize
left, right = 0, 0

while right < N and left <= right:
    if nums[right] - nums[left] < M:
        right += 1
    else:
        result = min(result, nums[right] - nums[left])
        left += 1

print(result)  