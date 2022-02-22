# https://www.acmicpc.net/problem/2798

from itertools import combinations
n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0

sum_list = set()
combi = list(combinations(data,3))
for c in combi:
    sum_list.add(sum(c))


## 오답
# sum_list = sorted(list(sum_list))
# for i in range(len(sum_list)):
#     if sum_list[i]>m:
#         print(sum_list[i-1])
#         break

for s in sum_list:
    if s <= m:
        result = max(result, s)
print(result)

# length = len(data)
# for i in range(0, length):
#     for j in range(i+1, length):
#         for k in range(j+1, length):
#             sum_value = data[i] + data[j] + data[k]
#             if sum_value<=m:
#                 result = max(result, sum_value)
# print(result)