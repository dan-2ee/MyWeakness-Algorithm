import sys

def isPrime(x):
    if (x==1):
        return 0
    for i in range(2, x):
        if (x%i==0):
            return 0
    
    return 1

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0
for num in numbers:
    cnt += (isPrime(num))

print(cnt)
