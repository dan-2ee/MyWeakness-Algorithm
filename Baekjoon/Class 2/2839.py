import sys


def divideSugar(n):
    cnt = 0
    while (n > 0):
        if (n % 5 == 0):
            cnt += (n//5)
            n %= 5
        else:
            cnt += 1
            n -= 3

    if (n < 0):
        return -1
    else:
        return cnt


n = int(sys.stdin.readline())
print(divideSugar(n))
