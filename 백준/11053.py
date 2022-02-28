# https://www.acmicpc.net/problem/11053
n = int(input())
data = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for j in range(0,i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
