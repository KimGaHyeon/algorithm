# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    a = sum(map(int, str(x)))
    if x%a==0:
        return True
    else:
        return False
print(solution(12))