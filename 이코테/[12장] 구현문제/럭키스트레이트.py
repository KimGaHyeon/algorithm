# https://www.acmicpc.net/problem/18406

n = input()

mid = len(n)//2
sum = 0

left = n[:mid]
right = n[mid:]

for i in left:
    sum += int(i)

for i in right:
    sum -= int(i)


if sum:
    print("READY")
else:
    print("LUCKY")