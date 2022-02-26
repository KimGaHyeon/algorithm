# https://www.acmicpc.net/problem/2747
'''
n = int(input())
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(n))
'''

n = int(input())
a, b = 0, 1

while n>0:
    a,b = b, a+b
    n -= 1
print(a)
