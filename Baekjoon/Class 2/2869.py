import sys

A, B, V = list(map(int, sys.stdin.readline().split()))
unit = A - B  # 하루에 이동하는 양 (낮, 밤 지났을 경우)
# V-A: A만큼 올라가서 정상에 도착하기 위해 지나야 할 날들
day = (V-A)//unit if ((V-A) % unit == 0) else ((V-A)//unit +1)
# 마지막 날에 A 만큼 이동해서 정상 도착 (B만큼 미끄러지지 않음)
print(day+1)   
