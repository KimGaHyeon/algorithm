# https://programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    cnt = x
    for _ in range(n):
        answer.append(cnt)
        cnt+=x
    return answer

