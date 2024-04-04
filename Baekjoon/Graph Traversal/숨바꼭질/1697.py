from collections import deque

N, K = map(int,input().split())
dq = deque([N])
MAX = 1000000
time = [0]*MAX

while dq:
    now = dq.popleft()  # 현재 위치 
    if now == K:  
        print(time[now])
        break
    for t in [now-1, now+1, now*2]:  # 이동위치 
        if 0<=t<MAX and time[t] == 0:  # time[t] != 0 인 경우, 이미 이전 시간에 방문했으므로 방문하지 않음 
            time[t] = time[now]+1
            dq.append(t)
