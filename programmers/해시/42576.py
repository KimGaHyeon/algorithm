# https://programmers.co.kr/learn/courses/30/lessons/42576
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant,completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion) :
        if p!=c:
            return p
    return participant[-1]

print(solution(participant,completion))