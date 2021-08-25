# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))

# def solution(d, budget):
#     answer = 0
#     if budget >= sum(d):
#         return len(d)
#     else:
#         # 제일 작은 부서부터 예산을 준다
#         d.sort()
#         for i in d:
#             if budget>=i:
#                 budget-=i
#                 answer+=1
#             else:
#                 return answer
#     return answer