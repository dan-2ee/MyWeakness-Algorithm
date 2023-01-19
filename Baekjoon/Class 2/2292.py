import sys

N = int(sys.stdin.readline())
honeyComb = 1
cnt = 1

while (honeyComb < N):
    honeyComb += (6*cnt)
    cnt += 1

print(cnt)
