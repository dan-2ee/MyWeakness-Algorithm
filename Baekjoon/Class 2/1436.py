import sys

n = int(sys.stdin.readline())
end = 666
order = 0

while(1):
    if ("666" in str(end)):
        order += 1
        if (order == n):
            print(end)
            break
    end += 1