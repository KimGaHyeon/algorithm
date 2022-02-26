'''
# parlindrome
def parlindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return parlindrome(s[1:-1])
    else:
        return False
print(parlindrome("asdf"))
print(parlindrome("level"))
'''


'''
연습문제 1
n이 홀수면 3*n+1 / 짝수면 n/2를, n이 1이 될때까지 반복하고 출력하는 함수 작성

def func(n):
    print(int(n))
    if n==1:
        return 1
    # 짝수
    if n%2==0:
        return func(n/2)
    else:
        return func(3*n+1)
print(func(3))
'''

'''
연습문제 2

정수 4를 1,2,3의 조합으로 나타내기
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
총 7가지

정수 n이 주어졌을 때, 1,2,3의 조합으로 만들 수 있는 경우의 수 출력하기
'''

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return func(n-1) + func(n-2) + func(n-3)

print(func(5))



