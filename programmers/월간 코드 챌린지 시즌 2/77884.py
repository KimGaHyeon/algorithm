# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if len(getDivisor(i))%2==0:
            answer += i
        else:
            answer -= i
    return answer


def getDivisor(n):
    divisors= []
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    return divisors


print(solution(13,17))