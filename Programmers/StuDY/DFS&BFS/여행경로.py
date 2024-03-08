def solution(tickets):
    route = {}
    for start, end in tickets:
        if (start in route):
            route[start].append(end)
        else:
            route[start] = [end]
    
    # 사전순으로 정렬
    for key in route:
        route[key].sort()

    answer, path = [], ['ICN']
    
    while path:
        start = path[-1]
        # 출발지가 없거나, 출발지에서 갈 수 있는 도착지가 없는 경우
        if start not in route or len(route[start]) == 0:
            answer.append(path.pop())
        else:
            path.append(route[start].pop(0))
    
    return answer[::-1]