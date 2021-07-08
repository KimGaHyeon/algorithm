# https://programmers.co.kr/learn/courses/30/lessons/70128
a = [1,2,3,4]
b = [-3,-1,0,2]

def solution(a, b):
    x = list(zip(a,b))
    answer = 0
    for a,b in x:
        answer += a*b
    return answer

print(solution(a,b))