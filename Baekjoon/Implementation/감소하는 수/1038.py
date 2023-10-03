from itertools import combinations

# 제일 큰 감소수: 9876543210
n = int(input())
lst = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        lst.append(int("".join(map(str, num))))

lst.sort()
print(lst[n]) if (n < len(lst)) else print(-1)
