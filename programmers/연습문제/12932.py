# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    n = str(n)
    n = n[::-1]
    return [int(i) for i in n]
print(solution(12345))