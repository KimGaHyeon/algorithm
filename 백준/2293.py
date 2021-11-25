n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
k = 10
d = [0] + [10001 for _ in range(k)]

for i in array:
    for j in range(array[i], k+1):
        if d[j-array[i]] != 10001:
            d[j]=min(d[j], d[j-array[i]]+1)

if d[k] == 10001:
    print(-1)
else:
    print(d[k])