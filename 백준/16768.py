n, k = map(int, input().split())
grid = [list(input()) for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def refresh(n):
    return [[False for _ in range(10)] for _ in range(n)]

check = refresh(n)
visited = refresh(n)

def dfs(x,y):
    visited[x][y] = True
    # 그룹의 크기
    size = 1
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy

        # 맵의 크기에 벗어나면
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue

        # 이미 방문했던 곳이거나, 다음에 이동할 곳이 현위치와 숫자가 다르다면(같은 그룹이 아니라면)
        if visited[nx][ny] or grid[x][y] != grid[nx][ny]:
            continue

        size += dfs(nx, ny)
    return size

def pop(x,y, val):
    check[x][y] = True
    grid[x][y] = 0
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy

        # 맵의 크기에 벗어나면
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue

        if check[nx][ny] or grid[x][y] != val:
            continue
        pop(nx,ny,val)

def down():
    # 세로줄
    for i in range(10):
        tmp = []
        for j in range(n):
            # 세로줄에서 0이 아닌것들을 다 넣음
            if grid[j][i] != '0':
                tmp.append(grid[j][i])
        for j in range(n-len(tmp)):
            grid[j][i] = '0'
        for j in range(n-len(tmp), n):
            grid[i][j] = tmp[j-(n-len(tmp))]


while True:
    change = False
    visited = refresh(n)
    check = refresh(n)

    for i in range(n):
        for j in range(10):
            # 0이거나 이미 방문한 곳이라면
            if grid[i][j] or visited[i][j]:
                continue
            size = dfs(i,j)
            if size >= k:
                pop(i,j,grid[i][j])
                # 변화가 일어난다면
                change = True
    if not change:
        break
    down()
for i in grid:
    print(''.join(i))
