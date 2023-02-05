import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    order = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    numbers = deque()
    if (n==0):
        _ = sys.stdin.readline()
        numbers = []
    else:
        numbers = deque(sys.stdin.readline().strip()[1:-1].split(","))
    
    isError, isReverse = 0, 0
    for i in order:
        if (i == "R"):
            isReverse = not(isReverse)
        elif (i == "D" and len(numbers) and isReverse):
            numbers.pop()
        elif (i == "D" and len(numbers) and not isReverse):
            numbers.popleft()
        else:
            isError = 1
            break
    if (isError):
        print("error")
    else:
        if (isReverse):
            numbers.reverse()
        result = list(numbers)
        print([]) if (result == []) else print('[' + ','.join(result) + ']')