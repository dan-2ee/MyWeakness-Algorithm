import sys
from collections import deque

n = int(sys.stdin.readline())

if (n == 1 or n == 2):
    print(n)
else:
    dq = deque()
    cnt = 2
    while(cnt <= n):   
        dq.append(cnt)
        cnt += 2
    if (n%2):  
        while(len(dq)!=1):
            dq.append(dq.popleft())
            if (len(dq) > 1):
                dq.popleft()
    else:
        while(len(dq)!=1):
            dq.popleft()
            if (len(dq) > 1):
                dq.append(dq.popleft())
    print(dq[0])