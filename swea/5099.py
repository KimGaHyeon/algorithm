import sys
sys.stdin = open("input/5099_input.txt", "r")
TC = int(input())

for tc in range(1, TC+1):
    N,M = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = []
    for i in range(N):
        queue.append([cheese[i], i])

    i = 0
    while len(queue)!=1:
        queue[0][0] //= 2
        if queue[0][0] == 0:
            if N+i < M:
                queue.pop(0)
                queue.append([cheese[N+i], N+i])
                i+=1
            elif N+i >= M:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

    print(f'#{tc} {queue[0][1]+1}')