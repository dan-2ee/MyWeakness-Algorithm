import sys

input = sys.stdin.readline
target = int(input())
N = int(input())  # 고장난 버튼의 수
brokenButton = list(input().strip().split()) if N else []

if target == 100:  
    print(0)
else:
    cnt = abs(target - 100)
    for channel in range(1000001):
        for c in str(channel):
            if c in brokenButton:
                break
        else:   # 고장나지 않은 버튼으로만 이루어진 경우
            cnt = min(cnt, len(str(channel)) + abs(channel - target))
    print(cnt)