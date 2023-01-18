import sys

numlst = sys.stdin.readline().split()
numlst = [int(i[::-1]) for i in numlst]

print(max(numlst))
