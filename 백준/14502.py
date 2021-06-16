# https://www.acmicpc.net/problem/14502

import sys
sys.stdin = open("input/연구소_input.txt", "r")
n,m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 0

def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 해당위치의 상하좌우에 바이러스가 퍼질수 있으면
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2  # 바이러스 전염시키고
                virus(nx,ny)    # 다시 그 자리에서 virus()

def getSafezone():
    safezone = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                safezone += 1
    return safezone

def dfs(wall):
    global result
    # 벽이 3개 세워진 경우
    if wall == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]

        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)

        result = max(result, getSafezone())
        return

    # 모든 가능한 곳에 벽 세우기
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                wall += 1
                dfs(wall)
                # 초기화
                data[i][j]=0
                wall -= 1

dfs(0)
print(result)