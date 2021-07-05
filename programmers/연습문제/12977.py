# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations
import math

nums = [1,2,7,6,4]

def solution(nums):
    answer = 0
    x = list(map(sum, combinations(nums, 3)))
    for i in x:
        if isPrime(i):
            answer += 1
    return answer

def isPrime(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

print(solution(nums))   