n = int(input())
money = 1000 - n
count = 0
data = [500, 100, 50, 10, 5, 1]
for d in data:
    while money >= d:
        money -= d
        count += 1

print(count)