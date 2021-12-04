# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    length = len(nums)//2
    nums = list(set(nums))
    for x in nums :
        if(answer < length):
            answer +=1
    return answer
