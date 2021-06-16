# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
import math

numbers = "17"
def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if isPrime(int(i)):
                answer.append(int(i))
    answer = len(set(answer))

    return answer



def isPrime(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

print(solution(numbers))
