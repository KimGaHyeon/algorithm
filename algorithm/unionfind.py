def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    parent[y] = x

parent = []
for i in range(0,5):
    parent.append(i)

union(1,4)
union(2,4)

for i in range(1, len(parent)):
    print(find(i), end=' ')
