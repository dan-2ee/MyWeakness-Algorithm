def fibo(n):
    if note[n] != [0, 0]:
        return note[n]
    else:
        tmp1, tmp2 = fibo(n-1), fibo(n-2)
        note[n] = [tmp1[0]+tmp2[0], tmp1[1]+tmp2[1]]
        return note[n]

T = int(input())
note = [[0,0] for _ in range(50)]
note[0], note[1] = [1, 0], [0, 1]

for _ in range(T):
    N = int(input())
    result = fibo(N)
    print(result[0], result[1])
