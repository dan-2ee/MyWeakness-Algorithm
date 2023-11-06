import sys

input = sys.stdin.readline
N = int(input())
maxTmp, minTmp = [0]*3, [0]*3
maxDp, minDp = [0]*3, [0]*3

for _ in range(N):
    a, b, c = map(int, input().split())

    for j in range(3):
        if j == 0:
            maxTmp[j] = a + max(maxDp[j], maxDp[j+1])
            minTmp[j] = a + min(minDp[j], minDp[j+1])
        elif j == 1:
            maxTmp[j] = b + max(maxDp[j-1], maxDp[j], maxDp[j+1])
            minTmp[j] = b + min(minDp[j-1], minDp[j], minDp[j+1])
        else:
            maxTmp[j] = c + max(maxDp[j-1], maxDp[j])
            minTmp[j] = c + min(minDp[j-1], minDp[j])

    for j in range(3):
        maxDp[j], minDp[j] = maxTmp[j], minTmp[j]

print(max(maxDp), min(minDp))