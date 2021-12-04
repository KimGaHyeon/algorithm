n,m = map(int, input().split())
balls = list(map(int, input().split()))
weight = [0]*(m+1)
count = 0

for ball in balls:
    weight[ball] += 1

for i in range(1, m+1):
    n -= weight[i]
    count += weight[i] * n

print(count)