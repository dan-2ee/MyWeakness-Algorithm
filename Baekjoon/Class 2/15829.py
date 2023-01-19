import sys
N = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

hash = 0
for i in range(N):
    hash += (ord(word[i]) - 96) * (31 ** i)

print(hash % 1234567891)
