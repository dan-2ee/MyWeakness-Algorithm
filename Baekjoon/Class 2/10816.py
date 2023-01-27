import sys
from collections import Counter

def binarySearch(start, end, target, lst):
    mid = (start + end)//2
    if (start > end):
        return 0
    elif (lst[mid] == target):
        return 1
    elif (lst[mid] > target):
        return binarySearch(start, mid-1, target, lst)
    else:
        return binarySearch(mid+1, end, target, lst)

_ = int(sys.stdin.readline())
numberCards = list(map(int, sys.stdin.readline().split()))   
numberCards.sort()
cnt = Counter(numberCards)

_ = int(sys.stdin.readline())
findCards = list(map(int, sys.stdin.readline().split()))   

for num in findCards:
    if not (binarySearch(0, len(findCards)-1, num, numberCards)):
        print(0, end=" ")
    else:
        print(cnt[num], end=" ")
print()