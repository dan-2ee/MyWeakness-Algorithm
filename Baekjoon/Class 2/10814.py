import sys

n = int(sys.stdin.readline())
people = [sys.stdin.readline().split() + [i] for i in range(n)]
people.sort(key=lambda x: (int(x[0]), x[2]))

for age, name, order in people:
    print(age, name)
