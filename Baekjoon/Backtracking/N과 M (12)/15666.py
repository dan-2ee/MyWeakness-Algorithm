import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []
for item in combinations_with_replacement(nums, M):
    if item not in result:
        result.append(item)
        print(" ".join(map(str, item)))