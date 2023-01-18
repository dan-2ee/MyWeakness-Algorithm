import sys

lst = list(map(int, sys.stdin.readline().split()))

if (lst == sorted(lst)):
    print("ascending")
elif (lst == sorted(lst, reverse=True)):
    print("descending")
else:
    print("mixed")
