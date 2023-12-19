from itertools import permutations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
perm = [per for per in set(permutations(nums, M))]
perm.sort()

for i in perm:
    print(" ".join(map(str, i)))
    