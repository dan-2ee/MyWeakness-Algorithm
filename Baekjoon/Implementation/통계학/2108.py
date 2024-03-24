import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

# 산술평균 
print(round(sum(nums)/N))
# 중간값
print(nums[N//2])
# 최빈값
commonlst = Counter(nums).most_common()
if len(commonlst) > 1 and commonlst[0][1] == commonlst[1][1]:  # 최빈값이 같은 경우
    print(commonlst[1][0])
else:
    print(commonlst[0][0])
# 범위
print(nums[N-1]-nums[0])