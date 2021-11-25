n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort()
max = 0
for i in range(n):
    if max < ropes[i]*(n-i):
        max = ropes[i]*(n-i)
print(max)