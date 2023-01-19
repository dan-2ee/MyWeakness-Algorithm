import sys

N = sys.stdin.readline().strip()

while (int(N)):
    result = "yes"
    for i in range(len(N)//2):
        if (N[i] != N[len(N)-i-1]):
            result = "no"
            break

    print(result)
    N = sys.stdin.readline().strip()
