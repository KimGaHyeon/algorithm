n, m = map(int,input().split())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 0

def getSafeZone(data):
    safeZone = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                safeZone += 1
    return safeZone

def virus():
    pass




