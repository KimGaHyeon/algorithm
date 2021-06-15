import sys
sys.stdin = open('input/5105_input.txt', 'r')

def check(i, j):
    return -1 < i < n and -1 < j < n and maze[i][j] != 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    global answer
    queue.append((x,y))
    visited.append((x, y))
    while queue:
        x,y=queue.pop(0)
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if check(nx,ny) and ((nx, ny) not in visited):
                queue.append((nx,ny))
                visited.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
                if maze[nx][ny] == 3:
                    answer=distance[nx][ny] - 1
                    return answer

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    maze = []
    for i in range(n):
        row = list(map(int,input()))
        if 2 in row:
            start = [i, row.index(2)]
        maze.append(row)
    visited = []
    queue = []
    distance = [[0]*n for _ in range(n)]
    answer = 0
    bfs(start[0], start[1])
    print(f'#{test_case} {answer}')