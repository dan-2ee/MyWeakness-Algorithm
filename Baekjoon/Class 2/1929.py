import sys

m, n = map(int, sys.stdin.readline().split())    
result = []
numbers = [False, False] + [True]*(n-1)   # 0,1은 False   
for i in range(2, m):       # 2부터 m전까지의 숫자
    if (numbers[i]):
        for j in range(i*2, n+1, i):
            numbers[j] = False

for i in range(m, n+1):     # m부터 n까지의 숫자
    if (numbers[i]):
        result.append(i)     # m이후의 소수 저장 
        for j in range(i*2, n+1, i):
            numbers[j] = False

for i in result:
    print(i)