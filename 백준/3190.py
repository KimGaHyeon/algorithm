# https://www.acmicpc.net/problem/3190

n = int(input())
k = int(input())

grid = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int, input().split())
    grid[a][b] = 1

l = int(input())
changes = []
for _ in range(l):
    x,c = input().split()
    changes.append((int(x),c))

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    # 왼쪽
    if c=='L':
        direction = (direction - 1) % 4
    # 오른쪽
    else:
        direction = (direction + 1) % 4
    return direction

def game():
    x,y = 1,1
    grid[x][y] = 2
    time = 0
    direction = 0
    snake = [(x,y)]
    index = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 내에 있고 뱀이 없는 위치라면
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and grid[nx][ny] != 2:
            # 사과가 없으면
            if grid[nx][ny] == 0:
                grid[nx][ny] = 2
                snake.append((nx,ny))
                sx, sy = snake.pop(0)
                grid[sx][sy] = 0

            # 사과가 있으면
            if grid[nx][ny] == 1:
                grid[nx][ny] = 2
                snake.append((nx,ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == changes[index][0]:
            direction = turn(direction, changes[index][1])
            index += 1
    return time

print(game())