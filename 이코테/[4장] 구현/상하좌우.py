n = int(input())
plan = input().split()
# 현재 위치
x, y = 1, 1
move = ['L','R','U','D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for p in plan:
    for i in range(len(move)):
        if p==move[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx > 4 or ny > 4 or nx < 1 or ny < 1:
        continue
    x, y = nx, ny

print(x,y)