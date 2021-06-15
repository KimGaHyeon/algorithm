# https://www.acmicpc.net/problem/11047
import sys
sys.stdin = open('input/동전_input.txt','r')
#
# def solution(data):
#     global k
#     answer = 0
#     for i in range(n):
#         if k//data[i] > 0:
#             answer += (k//data[i])
#             k -= data[i] * (k//data[i])
#     return answer
#
# n, k = map(int, input().split())
# data = []
# for i in range(n):
#     data.append(int(input()))
# print(sorted(data,reverse=True))
# data.sort(reverse=True)
#
# print(solution(data))


n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)

def solution(data):
    global k
    count = 0
    for d in data:
        count += k // d
        k %= d
    return count
print(solution(data))