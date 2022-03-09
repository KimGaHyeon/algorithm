# https://www.acmicpc.net/problem/1697
from collections import deque
n, k = map(int, input().split())
array = [0] * 100001

def bfs():
    queue = deque([n])
    while queue:
        now = queue.popleft()
        if now == k:
            return array[now]
        for next in (now+1, now-1, now*2):
            if 0 <= next < 100001 and not array[next]:
                array[next] = array[now] + 1
                queue.append(next)
print(bfs())
