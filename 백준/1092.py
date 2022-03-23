import sys
n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
checked = [False]*m
position = [0]*n
result, count = 0, 0
if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

while True:
    if count == len(boxes):
        break
    # 모든 크레인에 대해서
    for i in range(n):
        while position[i] < len(boxes):
            if not checked[position[i]] and cranes[i] >= boxes[position[i]]:
                checked[position[i]] = True
                position[i] += 1
                count += 1
                break
            position[i] += 1
    result += 1

print(result)