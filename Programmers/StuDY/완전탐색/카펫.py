def solution(brown, yellow):
    carpet = brown + yellow
    for i in range(1, carpet//2+1):
        # 가로 >= 세로
        if (carpet%i==0):
            w, h = carpet//i, i
            if (w-2)*(h-2) == yellow:
                return [w, h]