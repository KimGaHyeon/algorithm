def p(n):
    d = [0] * (n+4)
    d[1] = 1
    d[2] = 1
    for i in range(3, n+4):
        d[i] = d[i - 3] + d[i - 2]
    return d[n]

tc = int(input())
for _ in range(tc):
    n = int(input())
    print(p(n))