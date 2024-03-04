def solution(priorities, location):
    q = [[idx, item] for idx, item in enumerate(priorities)]
    execute = 0     # 실행 순서
    while (True):
        idx, item = q.pop(0)
        if item != max(priorities):
            q.append([idx, item])
        else:
            priorities.remove(item)
            execute += 1
            if idx == location:
                return execute