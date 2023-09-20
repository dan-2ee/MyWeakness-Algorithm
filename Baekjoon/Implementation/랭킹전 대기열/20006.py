import sys

input = sys.stdin.readline
p, m = map(int, input().split())        # 플레이어수, 방의 정원
people, room = [], []

for _ in range(p):
    level, name = input().split()
    people.append([int(level), name])

for level, name in people:
    isIn = False
    for r in room:
        if (len(r) >= m):
            continue 
        stdLevel = r[0][0]
        if (stdLevel - 10 <= level <= stdLevel + 10):
            r.append([level, name])
            isIn = True
            break
    # 어떤 방에도 들어가지 못하면 새로운 방 생성 
    if (not isIn):
        room.append([[level, name]])
   
for i in range(len(room)):
    room[i].sort(key=lambda x : x[1])
    print("Started!") if (len(room[i]) == m) else print("Waiting!")
    for level, name in room[i]:
        print(level, name)
