# https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    answer = ''
    answer += "*"*len(phone_number[0:-4])
    answer += phone_number[-4:]
    return answer

phone_number=  "01033334444"

print(solution(phone_number))