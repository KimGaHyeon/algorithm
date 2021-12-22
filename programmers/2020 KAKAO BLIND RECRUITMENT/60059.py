def rotate(arr):
    return list(zip(*arr[::-1]))

def attach(x, y, m, key, grid):
    for i in range(m):
        for j in range(m):
            grid[x + i][y + j] += key[i][j]


def detach(x, y, m, key, grid):
    for i in range(m):
        for j in range(m):
            grid[x + i][y + j] -= key[i][j]


def check(grid, m, n):
    for i in range(n):
        for j in range(n):
            if grid[m + i][m + j] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)
    grid = [[0] * (m * 2 + n) for _ in range(m * 2 + n)]

    # 가운데에 자물쇠 배치
    for i in range(n):
        for j in range(n):
            grid[m + i][m + j] = lock[i][j]

    rotated_key = key

    # 4방향 확인
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, m + n):
            for y in range(1, m + n):
                attach(x, y, m, rotated_key, grid)
                if check(grid, m, n):
                    return True
                detach(x, y, m, rotated_key, grid)
    return False