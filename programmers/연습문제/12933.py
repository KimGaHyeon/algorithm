# https://programmers.co.kr/learn/courses/30/lessons/12933
n = 118372
def solution(n):
    n = str(n)
    return int(''.join(sorted(n, reverse=True)))
print(solution(n))
