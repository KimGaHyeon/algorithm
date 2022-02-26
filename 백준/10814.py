# https://www.acmicpc.net/problem/10814
n = int(input())
members = []
for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

members = sorted(members, key=lambda x: x[0])

for member in members:
    print(member[0], member[1])
