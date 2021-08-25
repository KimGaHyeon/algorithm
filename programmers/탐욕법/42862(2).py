# https://programmers.co.kr/learn/courses/30/lessons/42862
n = 5
lost = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    # 여벌이 있던 학생 중 안 잃어버린 학생 (빌려줄수 있는 학생)
    _reserve = [r for r in reserve if r not in lost]
    # 체육복을 잃어버린 학생 중 여벌이 없는 학생 (빌려야 하는 학생)
    _lost = [l for l in lost if l not in reserve]
    _reserve.sort()
    _lost.sort()
    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)
    return n - len(_lost)
