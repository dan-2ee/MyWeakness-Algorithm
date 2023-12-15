from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
comb = [data for data in combinations_with_replacement(nums, M)]
for i in sorted(comb):
    print(" ".join(map(str, i)))