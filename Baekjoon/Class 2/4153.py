import sys

while (True):
    numlst = sorted(list(map(int, sys.stdin.readline().split())))
    if not (sum(numlst)):
        break
    elif (numlst[0]**2 + numlst[1]**2 == numlst[2]**2):
        print("right")
    else:
        print("wrong")
