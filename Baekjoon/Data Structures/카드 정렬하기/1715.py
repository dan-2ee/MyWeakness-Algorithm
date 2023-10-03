import sys
import heapq

def findCnt(cards):
    cnt = 0
    while(len(cards) > 1):
        first, snd = heapq.heappop(cards), heapq.heappop(cards)
        tmp = first + snd
        cnt += tmp
        heapq.heappush(cards, tmp)
    return cnt
        
input = sys.stdin.readline
N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

print(findCnt(cards))