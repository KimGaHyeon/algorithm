
'''
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
for i in data:
    print(i)
'''
# selection sort
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if data[min_index] > data[j]:
            min_index = j
    data[min_index], data[i] = data[i], data[min_index]

for i in data:
    print(i)