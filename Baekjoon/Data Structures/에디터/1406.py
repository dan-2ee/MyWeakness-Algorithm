import sys
from collections import deque

input = sys.stdin.readline
dq = deque(list(input().strip()))
T = int(input())
N = len(dq)
cursor = N   # 맨 오른쪽에 위치 

for _ in range(T):
    command = input().split()
    if (command[0] == "L" and cursor > 0):
        cursor -= 1
    elif (command[0] == "D" and cursor < N):
        cursor += 1
    elif (command[0] == "B" and cursor > 0):
        del dq[cursor-1]
        cursor -= 1
    elif (command[0] == "P"):
        dq.insert(cursor, command[1])
        cursor += 1

print("".join(dq))