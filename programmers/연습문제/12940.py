# https://programmers.co.kr/learn/courses/30/lessons/12940
from math import gcd
def solution(n, m):
    return [gcd(n,m)] + [n*m // gcd(n,m)]

print(solution(2,5))