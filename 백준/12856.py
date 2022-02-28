n,k = map(int, input().split())
table = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    weight, value = map(int, input().split())
    for j in range(1, k+1):
        if j < weight:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(table[i-1][j], table[i-1][j-weight] + value)
print(table[n][k])
