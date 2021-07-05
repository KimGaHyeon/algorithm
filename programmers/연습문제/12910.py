#https://programmers.co.kr/learn/courses/30/lessons/12910
arr = [5, 9, 7, 10]
divisor = 5

def solution(arr, divisor):
    ans = [i for i in arr if i % divisor == 0]
    if not ans:
        ans.append(-1)
    return sorted(ans)
