import sys

def dfs(start, person):
    for i in range(N):
        if graphs[person][i] and i!=start:
            return True
    return False



input = sys.stdin.readline
N, M = list(map(int, input().split()))   # 사람의 수, 관계의 수
graphs = [[False] * N for _ in range(N)]

for _ in range(M):
    line = list(map(int, input().split()))
    graphs[line[0]][line[1]] = True

person = [i for i in range(N)]

while person:
    start = person[0]
    person.remove(start)
    for idx, value in enumerate(graphs[start]):
        if value:
            result = dfs(start, idx)
            if result:
                print(1)
                sys.exit()

print(0)
    

    
    



