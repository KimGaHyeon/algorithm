graph = dict()
graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

'''
    A
   / \
  B   C
 /   /|\  
D   G H I 
|\      |     
E F     J
'''



def bfs(graph, start):
    visited = []
    need_visit = []

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

def dfs(graph, start):
    visited, need_visit = [], []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

print(bfs(graph,'A'))
print(dfs(graph,'A'))


