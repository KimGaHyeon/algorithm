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
    a_count, b_count, c_count = 0,0,0

    for i,answer in enumerate(answers):
        if answer == a[i%5]:
            a_count+=1
        if answer == b[i%8]:
            b_count+=1
        if answer == c[i%10]:
            c_count+=1

    count = {1: a_count, 2: b_count, 3: c_count}
    top = max(count.values())
    result = [k for k,v in count.items() if v==top]
    return result
print(solution(answers))




