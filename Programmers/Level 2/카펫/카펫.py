def solution(brown, yellow):
    answer = []
    for i in range(yellow//2+1, 0, -1):
        if yellow % i == 0:
            x, y = i, yellow // i
            if (x+2)*2 + (y*2) == brown:
                answer = [x+2, y+2]
                break
    return answer