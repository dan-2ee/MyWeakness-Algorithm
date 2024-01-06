def solution(a, b):
    if (b==1):
        return a % C
    remain = solution(a, b//2)
    if (b%2==0):
        return remain * remain % C
    else:
        return remain * remain * a % C
A, B, C = map(int, input().split())
print(solution(A,B))
# other solution
# print(pow(A, B, C))