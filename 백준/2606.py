# https://www.acmicpc.net/problem/2606
from collections import deque
n = int(input())
m = int(input())
network = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

def bfs(network, start):
    need_visit = deque([start])
    visited = []
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(network[node])
    return len(visited)-1

print(bfs(network, 1))



