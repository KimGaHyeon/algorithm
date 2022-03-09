from collections import deque
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
test_case = int(input())

def bfs(array, a, b):
    queue = deque()
    queue.append((a,b))
    array[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if array[nx][ny]:
                array[nx][ny] = 0
                queue.append((nx, ny))
    return


def dfs(array, x, y):
    # 배추가 없거나 이미 방문했던 곳이라면 방문하지 않음
    if not array[x][y]:
        return

    # 시작점 방문 처리
    array[x][y] = 0
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 배추가 없거나 이미 방문했던 곳이라면 방문하지 않음
        if not array[nx][ny]:
            continue
        # 상하좌우에 대해서 다시 dfs
        dfs(array, nx, ny)


for _ in range(test_case):
    answer = 0
    n,m,k = map(int, input().split())
    array = [[0] * m for _ in range(n)]

    for _ in range(k):
        x,y = map(int, input().split())
        array[x][y] = 1

    for i in range(n):
        for j in range(m):
            if array[i][j]:
                dfs(array, i, j)
                answer += 1
    print(answer)