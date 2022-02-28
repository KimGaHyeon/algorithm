# https://www.acmicpc.net/problem/1074
def z(n,r,c):
    global result

    if n == 2:
        if r == R and c == C:
            print(result)
            return
        result += 1
        if r == R and c+1 == C:
            print(result)
            return
        result += 1
        if r+1 == R and c == C:
            print(result)
            return
        result += 1
        if r+1 == R and c+1 == C:
            print(result)
            return
        result += 1
        return
    z(n/2, r, c)
    z(n/2, r, c+n/2)
    z(n/2, r+n/2, c)
    z(n/2, r+n/2, c+n/2)

result = 0
N,R,C = map(int, input().split())
z(2**N, 0, 0)


