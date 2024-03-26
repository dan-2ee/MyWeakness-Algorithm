import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    command = input().strip()
    N = int(input())
    nums = list(input().strip()[1:-1].split(','))
    nums = deque(nums) if N!=0 else []
    reversed = 0
    for c in command:
        if c == 'R':
            reversed = (not reversed)
        elif c == 'D' and not reversed and nums:
            nums.popleft()
        elif c == 'D' and reversed and nums:
            nums.pop()
        else:
            nums = 'error'
            break
    
    if nums == 'error':
        print('error')
    else:
        if reversed: nums.reverse()
        print("["+",".join(list(nums))+"]")