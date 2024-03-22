import sys
from collections import deque

input = sys.stdin.readline
T = int(input())  # 테스트 케이스 개수 

for _ in range(T):
    n, target = map(int, input().split())   # 문서 개수, 찾고자하는 문서의 위치
    documents = list(map(int, input().split()))
    dq = deque((priority, idx==target) for idx, priority in enumerate(documents))  # (우선 순위, 타겟여부)
    order = 0
    while (True):
        if (dq[0][0] == max(dq)[0]):  # 가장 높은 우선순위면 인쇄
            _, isTarget = dq.popleft()
            order += 1
            if (isTarget):  # 찾고자 하는 아이템일경우
                break
        else:   # 아닌 경우 가장 뒤에 재배치
            dq.append(dq.popleft())
    print(order)