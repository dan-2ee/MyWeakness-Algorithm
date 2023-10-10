import sys

input = sys.stdin.readline
N = int(input())
words = [input().strip() for _ in range(N)]

values = {}
for word in words:
    idx = 1
    l = len(word)
    for char in word:
        if char in values:
            values[char] += (10 ** (l-idx))
        else:
            values[char] = (10 ** (l-idx))
        idx+=1

cnt = 9
values = dict(sorted(values.items(), key=lambda x:x[1], reverse=True))
for key, value in values.items():
    values[key] = cnt
    cnt -= 1

res = []
for word in words:
    tmp = ""
    for char in word:
        tmp += str(values[char])
    res.append(int(tmp))

print(sum(res))

