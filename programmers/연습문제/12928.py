# https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = []
    for i in range(n+1):
        if n%i==0:
            answer.append(i)
    return sum(answer)