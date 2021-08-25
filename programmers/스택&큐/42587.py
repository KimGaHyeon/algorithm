# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

# def solution(priorities, location):
#     answer = 0
#     queue = deque([(v,i) for i,v in enumerate(priorities)])
#     print(queue)
#     while len(queue):
#         item = queue.popleft()
#         if queue and max(queue)[0] > item[0]:
#             queue.append(item)
#         else:
#             answer += 1
#             if item[1]==location:
#                 break
#     return answer


def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))