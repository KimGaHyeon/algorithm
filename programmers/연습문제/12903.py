# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    mid = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[mid]
    else:
        return s[mid-1:mid+1]
