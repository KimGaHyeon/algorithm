# https://programmers.co.kr/learn/courses/30/lessons/42840
"""
12345/12345/12345/

2/123/2/4/2/5/2/123/2/4/2/5

33/11/22/44/55/33/11/22/44/55
"""

answers = [1,2,3,4,5]

def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = {'1':0, '2':0, '3':0}
    for i,answer in enumerate(answers):
        if answer == a[i%5]:
            count['1']+=1
        if answer == b[i%8]:
            count['2']+=1
        if answer == c[i%10]:
            count['3']+=1


    for i in count.keys():
        if count[i] == max(count.values()):
            return i

print(solution(answers))