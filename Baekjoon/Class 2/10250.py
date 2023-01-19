import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = list(map(int, sys.stdin.readline().split()))
    if (N % H):   # N이 H의 배수일 때
        y = N % H
        x = (N // H) + 1
    else:
        y = H
        x = N // H
    print(y*100 + x)
