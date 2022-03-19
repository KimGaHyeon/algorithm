# https://www.acmicpc.net/problem/1439
s = input()
change = 0
for i in range(1, len(s)):
  if s[i] != s[i-1]:
    change += 1

print((change+1)//2)