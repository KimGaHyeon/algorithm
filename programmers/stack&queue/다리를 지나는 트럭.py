# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = deque([0]*bridge_length, maxlen=bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    while queue:
        # queue.pop()
        out = queue.popleft()
        bridge_weight -= out

        time+=1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                left = truck_weights.popleft()
                bridge_weight += left
                queue.append(left)
            else:
                queue.append(0)

        # if truck_weights:
        #     if (sum(queue) + truck_weights[0]) <= weight :
        #         queue.appendleft(truck_weights.pop(0))
        #     else:
        #         queue.appendleft(0)
    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length,weight,truck_weights))

