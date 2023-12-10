import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
LIS = [1] * N  # 왼쪽 - 증가 수열
LDS = [1] * N  # 오른쪽 - 감소 수열 

for i in range(1, N):
    for j in range(i):
        if (nums[i] > nums[j]):
            LIS[i] = max(LIS[i], LIS[j]+1)

for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if (nums[i] > nums[j]):
            LDS[i] = max(LDS[i], LDS[j]+1)


result = 0
for standard in range(N):
    left, right = 0, 0
    if (standard < N-1):
        # 오른쪽 - 감소 수열 확인
        for i in range(standard+1, N):
            if (nums[standard] > nums[i]):
                right = max(right, LDS[i])
        
    if (standard > 0):
        # 왼쪽 - 증가 수열 확인
        for i in range(standard):
            if (nums[standard] > nums[i]):
                left = max(left, LIS[i])
    result = max(result, left + right + 1)

print(result)