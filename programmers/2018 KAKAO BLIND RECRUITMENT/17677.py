# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    lst1 = []
    lst2 = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            lst1.append(str1[i] + str1[i + 1])

    for j in range(len(str2) - 1):
        if str2[j].isalpha() and str2[j + 1].isalpha():
            lst2.append(str2[j] + str2[j + 1])

    cnt1 = Counter(lst1)
    cnt2 = Counter(lst2)

    inter = list((cnt1 & cnt2).elements())
    union = list((cnt1 | cnt2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)