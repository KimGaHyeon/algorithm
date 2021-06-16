# https://www.acmicpc.net/problem/11399
import sys
sys.stdin = open("input/ATM_input.txt", "r")

n = int(input())
p = list(map(int, input().split()))
p.sort()

sum = 0
for i in range(n):
    for j in range(i+1):
        sum += p[j]
print(sum)