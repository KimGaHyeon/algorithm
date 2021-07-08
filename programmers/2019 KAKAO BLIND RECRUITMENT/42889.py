# https://programmers.co.kr/learn/courses/30/lessons/42889


stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
def solution(N, stages):
    result = {}
    num = len(stages)
    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)
solution(N, stages)

