import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

def BlackJack():
    findMax = 0
    for i in range(n-2):   
        for j in range(i+1, n-1):   
            for k in range(j+1, n):   
                item = cards[i] + cards[j] + cards[k]
                if (item <= m and item > findMax):
                    findMax = item
    
    return findMax

print(BlackJack())