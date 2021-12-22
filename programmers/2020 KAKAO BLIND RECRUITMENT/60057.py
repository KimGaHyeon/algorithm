# https://programmers.co.kr/learn/courses/30/lessons/60057
# def solution(s):
#     answer = len(s)
#     for step in range(1,len(s)//2+1):
#         compressed = ""
#         prev = s[0:step]
#         count = 1
#         for j in range(step, len(s), step):
#             if prev==s[j:j+step]: # 압축되는 경우
#                 count += 1
#             else: # 압축 안되는 경우
#                 compressed += str(count) + prev if count>=2 else prev
#                 prev = s[j:j+step]
#                 count = 1
#         compressed += str(count) + prev if count>=2 else prev
#         answer = min(answer, len(compressed))
#     return answer

def solution(s):
    for unit in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:unit]
        count = 1
        for i in range(unit, len(s), unit):
            if prev==s[i:i+unit]:
                count += 1
        else:
            compressed += str(count) + prev if count>=2 else prev
            prev = s[i:i+unit]
            count = 1
        compressed += str(count) + prev if count >= 2 else prev
    return min(len(s), len(compressed))
solution("aabbacc")
