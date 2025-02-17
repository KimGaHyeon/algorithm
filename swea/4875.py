import sys
sys.stdin = open('input/4875_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    stack = []  # 현재 위치
    result = 0
    maze = [list(map(int, list(input()))) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                stack.append((i, j))
                visit[i][j] = 1
    while stack:
        x, y = stack.pop()
        if maze[x][y] == 3:
            result = 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
                stack.append((nx, ny))
                visit[nx][ny] = 1
    print('#{} {}'.format(test_case, result))
