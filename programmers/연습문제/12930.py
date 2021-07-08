# https://programmers.co.kr/learn/courses/30/lessons/12930
s="try hello world"
def solution(s):
    answer = ''
    for word in s.split(" "):
        n = ''
        for i in range(len(word)):
            if i%2 == 0 :
                n += word[i].upper()
            else :
                n += word[i].lower()
        answer += (n + " ")
    return answer[0:-1]
