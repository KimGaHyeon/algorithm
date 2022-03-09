# https://www.acmicpc.net/problem/1325
from collections import deque
n, m = map(int, input().split())
data = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[b].append(a)

def bfs(v):
    queue = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    cnt = 1

    while queue:
        node = queue.popleft()
        for i in data[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

result = []
max_val = -1
for i in range(1,n+1):
    x = bfs(i)
    if x > max_val:
        result = [i]
        max_val = x
    elif x == max_val:
        result.append(i)
        max_val = x

for i in result:
    print(i, end=" ")
