import sys


def GCD(a, b):
    while (b):
        tmp = a
        a, b = b, tmp % b
    return a


def LCM(a, b, gcd):
    return a * b // gcd


a, b = list(map(int, sys.stdin.readline().split()))
gcd = GCD(a, b)
lcm = LCM(a, b, gcd)
print(gcd)
print(lcm)
