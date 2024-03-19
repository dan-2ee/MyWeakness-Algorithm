def solution(n, costs):
    costs.sort(key=lambda x:x[2])  # 소모비용 순으로 정렬 
    visited = set([costs[0][0], costs[0][1]])  # 시작 노드 추가
    answer = costs[0][2]
    while (len(visited) != n):
        for start, end, cost in costs[1:]:
            if (start in visited and end in visited):  # 이미 연결된 지점일 경우 
                continue
            if (start in visited or end in visited):  
                visited.update([start, end])
                answer += cost
                break
    return answer