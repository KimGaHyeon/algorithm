# https://programmers.co.kr/learn/courses/30/lessons/81302
import queue

# 상하좌우 행렬 델타값 정의
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(place, row, col):
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = queue.Queue()
    visited[row][col] = True
    q.put((row, col, 0))  # enqueue, (row, col, 거리값)

    while not q.empty():
        curr = q.get()  # dequeue
        if curr[2] > 2:
            continue  # 거리가 2 초과하면 탐색 종료
        # 자기 자신이 아니면서 거리가 2 이하인 곳에 P가 있다면
        if curr[2] != 0 and place[curr[0]][curr[1]] == "P":
            return False

        # 거리 2 이하에서 다른 P를 만나지 않았으면 이동
        for i in range(4):
            nr = curr[0] + d[i][0]
            nc = curr[1] + d[i][1]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            if visited[nr][nc]:
                continue
            if place[nr][nc] == "X":
                continue

            visited[nr][nc] = True
            q.put((nr, nc, curr[2] + 1))
    return True


def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                if bfs(place, r, c) == False:
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer