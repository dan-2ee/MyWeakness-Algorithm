import sys


def findBC(n, k):
    if (n == k or k == 0):    # 파스칼 삼각형 기준, 맨 왼쪽과 맨 오른쪽 1
        return 1
    else:
        return findBC(n-1, k-1) + findBC(n-1, k)


n, k = list(map(int, sys.stdin.readline().split()))
print(findBC(n, k))
