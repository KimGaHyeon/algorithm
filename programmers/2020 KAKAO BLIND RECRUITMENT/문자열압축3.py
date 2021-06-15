import math

def compress(s, cut):
    pivot = s[0:cut]
    rst = len(pivot)
    count = 1
    for i in range(cut, len(s), cut):
        if pivot == s[i:i+cut]:
            count += 1
        else:
            if count != 1:
                rst += len(str(count))
            count = 1
            pivot = s[i:i+cut]
            rst += len(pivot)
    if count != 1:
        rst += len(str(count))
    return rst


def solution(s):
    if len(s)<=2:
        return len(s)
    answer = math.inf
    for i in range(1, len(s)//2 + 1):
        answer = min(answer, compress(s, i))

    return answer

