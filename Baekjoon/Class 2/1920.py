import sys


def binarySearch(lst, target, start, end):
    mid = (start + end)//2
    if (start > end):
        return 0
    elif (numLst[mid] == target):
        return 1
    elif (numLst[mid] > target):
        return binarySearch(lst, target, start, mid-1)
    else:
        return binarySearch(lst, target, mid+1, end)


n = int(sys.stdin.readline())
numLst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
findNumLst = list(map(int, sys.stdin.readline().split()))
numLst.sort()

for target in findNumLst:
    print(binarySearch(numLst, target, 0, n-1))
