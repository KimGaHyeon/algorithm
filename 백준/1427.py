# https://www.acmicpc.net/problem/1427
# n = input()
# data = []
# for i in n:
#     data.append(i)
# data.sort(reverse=True)
# x = int(''.join(data))
# print(x)

data = input()
for i in range(9, -1, -1):
    for j in data:
        if int(j) == i:
            print(i, end="")

