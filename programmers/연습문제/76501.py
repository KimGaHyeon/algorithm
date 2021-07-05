# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes,signs))


# def solution(absolutes, signs):
#     for i in range(len(absolutes)):
#         if signs[i]==False:
#             absolutes[i] *= -1
#     return sum(absolutes)

absolutes = [4,7,12]
signs = [True, False, True]

solution(absolutes,signs)