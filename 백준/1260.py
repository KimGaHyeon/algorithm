# https://www.acmicpc.net/problem/1260
n, m, v = map(int, input().split());
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start):
    visited, need_visit = [], []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    for i in visited:
        print(i, end=" ")

def bfs(graph, start):
    visited, need_visit = [], []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    for i in visited:
        print(i, end=" ")

for i in graph:
    i.sort(reverse=True)
dfs(graph,v)
print("")
for i in graph:
    i.sort()
bfs(graph,v)
