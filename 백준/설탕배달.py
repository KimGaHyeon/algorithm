# https://www.acmicpc.net/problem/2839
import sys
sys.stdin = open("input/설탕배달_input.txt", "r")

n = int(input())
count = 0
def solution(n):
    count = 0
    while n >= 0:
        if n % 5 == 0:
            count += (n//5)
            print(count)
            break
        n -= 3
        count += 1
    else:
        print(-1)

solution(n)