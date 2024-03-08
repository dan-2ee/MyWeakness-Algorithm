def solution(tickets):
    route = {}
    for start, end in tickets:
        if (start in route):
            route[start].append(end)
        else:
            route[start] = [end]
    
    # 사전 역순으로 정렬
    for key in route:
        route[key].sort(reverse=True)

    answer, path = [], ['ICN']
    while path:
        start = path[-1]
        # 경로가 없거나 출발지가 없는 경우, 도착
        if start not in route or len(route[start]) == 0:
            answer.append(path.pop())
        else:
            path.append(route[start].pop())
    return answer[::-1]