x = input()
y = input()
len_x = len(x)
len_y = len(y)

dp = [[0] * (len_y+1) for _ in range(len_x+1)]

for i in range(1, len_x+1):
    for j in range(1, len_y+1):
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len_x][len_y])
