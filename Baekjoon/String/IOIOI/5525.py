import sys

input = sys.stdin.readline
N = int(input())
L = int(input())  
S = input().strip()

idx, answer, count = 0, 0, 0

while (idx < L-2):
    if S[idx:idx+3] == "IOI":
        count += 1
        idx += 2
        if count == N:
            answer += 1
            count -= 1
    else:
        idx += 1
        count = 0

print(answer)