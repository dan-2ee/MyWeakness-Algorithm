def solution(routes):
    routes.sort()
    answer = 0
    now = routes[0]   # 현재 카메라 위치 
    for start, end in routes[1:]:
        if (now[1] >= start):  # 카메라가 끝나는 시점 >= 현재 루트 진입 시점
            now = [start, min(now[1], end)]
        else:  # 카메라 위치 보다 진입 시점이 바깥에 있는 경우
            answer += 1
            now = [start, end]
    # 마지막 루트 카메라 더해줌
    return answer+1