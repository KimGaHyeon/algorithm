import sys
sys.stdin = open("input/4869_input.txt", "r")
T = int(input())

def dp(x):
    if x==N:
        return 1
    if x>N:
        return 0
    return dp(x+10)+dp(x+20)*2

for test_case in range(1, T + 1):
    N = int(input())
    print("#%s %d"%(test_case, dp(0)))
