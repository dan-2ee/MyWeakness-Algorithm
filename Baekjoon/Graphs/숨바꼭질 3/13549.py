from collections import deque

def bfs():
    dq = deque()
    dq.append(1) if (N == 0) else dq.append(N)

    while (dq):
        current = dq.popleft()
        if (time[K]!=0 or current == K):
            return time[K]
        
        for i in [current-1, current+1, current*2]:
            if (0<=i<limit and time[i] == 0):
                if (i == current*2):
                    time[i] = time[current]
                    dq.appendleft(i)
                else:
                    time[i] = time[current]+1
                    dq.append(i)
                    
limit = 100001
N, K = map(int, input().split())
time = [0] * limit
result = bfs()

print(result+1) if (N == 0) else print(result)