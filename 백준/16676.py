# https://www.acmicpc.net/problem/16676
n = input()
s = '1'*len(n)
if len(n) == 1:
    print(1)
elif int(n) >= int(s):
    print(len(n))
else:
    print(len(n)-1)