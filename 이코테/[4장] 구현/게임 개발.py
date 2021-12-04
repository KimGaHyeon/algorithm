n,m = map(int, input().split())
x,y,direction = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == 0:
        direction = 3

count = 1
turned = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 방문 가능하면
    if visited[nx][ny] == 0 and grid[nx][ny] == 0:
        # 방문 마킹
        visited[nx][ny] = 1
        x,y = nx, ny
        count += 1
        turned = 0
        continue
    else:
        turned += 1

    # 상하좌우 다 봤는데 갈곳이 없다면
    if turned == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 이동할 수 있다면 이동
        if grid[nx][ny]==0:
            x,y = nx, ny
        else:
            break
        turned = 0

print(count)