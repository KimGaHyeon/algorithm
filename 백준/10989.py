# https://www.acmicpc.net/problem/10989
import sys
n = int(sys.stdin.readline())
data = [0] * 10001
for _ in range(n):
    x = int(sys.stdin.readline())
    data[x] += 1

for i in range(len(data)):
    if data[i]!=0:
        for _ in range(data[i]):
            print(i)