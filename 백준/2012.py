# https://www.acmicpc.net/problem/2012

n = int(input())
rank = []
complain = 0
for _ in range(n):
    rank.append(int(input()))

rank.sort()
for i in range(1, len(rank)+1):
    complain += abs(i-rank[i-1])
print(complain)