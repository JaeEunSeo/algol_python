'''
시간초과 오류 : sum 함수가 시간을 많이 소요하므로, 
변수에서 가감하는 식으로 설정
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    # 현재 다리에 올라간 무게 : sum(bridge)
    bridge = deque([0] * bridge_length)
    cur_weight = sum(bridge)
    while True:
        if not bridge and len(truck_weights) == 0:
            break
        time += 1
        cur_weight -= bridge.popleft()
        if truck_weights:
            if truck_weights[0] + cur_weight <= weight:
                bridge.append(truck_weights.pop(0))
                cur_weight += bridge[-1]
            else:
                bridge.append(0)
    return time

print(solution(11,111, [11, 1, 111, 11, 1, 1, 1, 111, 1, 111, 11, 11, 11, 1]))