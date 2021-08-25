# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    count, countzero = 0,0
    rank = [6,6,5,4,3,2,1]
    answer = [0,0]
    for i in lottos:
        if i==0:
            countzero+=1
        if i in win_nums:
            count+=1
    answer[0], answer[1] = rank[count+countzero], rank[count]

    return answer