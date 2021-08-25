# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    while num!=1:
        if num%2==0: num %= 2
        else: num = num*3 + 1
    return num