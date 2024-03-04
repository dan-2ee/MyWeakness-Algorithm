# bridge_length = 이동 시간, 다리에 올라갈 수 있는 트럭 수
# weight = 다리가 견딜 수 있는 무게
# truck_weights = 트럭 별 무게

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length  # 현재 다리 상태
    total_weight = 0  # 다리에 있는 트럭 무게
    while bridge:
        time += 1
        moving_truck = bridge.pop(0)  
        total_weight -= moving_truck  # 다리에서 맨 앞의 트럭 제거
        if truck_weights:  # 대기 상태인 트럭이 남아 있는 경우
            if total_weight + truck_weights[0] <= weight:
                # 다리에 트럭 추가 가능하면 추가
                truck = truck_weights.pop(0)
                bridge.append(truck)  
                total_weight += truck
            else:
                # 추가 불가능하면 0 추가하여 다리 길이 유지
                bridge.append(0)  
    return time