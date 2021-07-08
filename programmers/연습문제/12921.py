# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    num_set = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num_set:
            num_set -= set(range(i*2, n+1, i))
    answer = len(num_set)
    return answer