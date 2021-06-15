# 인접행렬
node = 4
edges = 5
nodes = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

adjacent = [[0 for _ in range(node)] for _ in range(node)]

for i,j in nodes:
    adjacent[i-1][j-1] = 1
    adjacent[j-1][i-1] = 1

print(adjacent)

n = 4
e = 5
nodes = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

adj = [[] for _ in range(n)]

for src, dst in nodes:
    adj[src-1].append(dst-1)
    adj[dst-1].append(src-1)

print(adj)