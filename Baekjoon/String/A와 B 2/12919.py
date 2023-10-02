import sys

def isSame(t):
    if t==s:
        print(1)
        sys.exit()
    if len(t)==0:
        return 0
    if t[-1]=='A': 
        isSame(t[:-1])
    if t[0]=='B': 
        isSame(t[1:][::-1]) 

input = sys.stdin.readline
s = input().strip()
t = input().strip()
isSame(t)
print(0)