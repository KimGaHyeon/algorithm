def dfsR(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfsR(graph, i, visited)

def dfs(graph, v, visited):
    stack = []
    stack.append(v)
    visited[v] = True
    while(stack):
        node = stack.pop()
        for adjacent in graph[node]:
            if visited[adjacent] == False:
                visited[adjacent] = True
                stack.append(adjacent)
        print(node)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]


visited = [False] * len(graph)

# dfsR(graph, 1, visited)
dfs(graph, 1, visited)