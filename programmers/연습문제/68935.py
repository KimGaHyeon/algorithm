# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = ''
    while n > 0:
        n, re = divmod(n, 3)  # n을 3으로 나눈 몫과 나머지
        answer += str(re)

    return int(answer, 3)  # 3진법 -> 10진법