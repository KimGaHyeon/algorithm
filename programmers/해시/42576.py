# https://programmers.co.kr/learn/courses/30/lessons/42576
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(s,c):
    s.sort()
    c.sort()
    for par, com in zip(s, c) :
        if par!=com:
            return par
    return s[-1]
print(solution(participant,completion))