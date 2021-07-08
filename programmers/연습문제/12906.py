# https://programmers.co.kr/learn/courses/30/lessons/12906
arr = [1,1,3,3,0,1,1]
def solution(arr):
    b = []
    for i in range(len(arr)):
        if i == 0:
            b.append(arr[i])
        elif arr[i]!=arr[i-1]:
            b.append(arr[i])
    return b