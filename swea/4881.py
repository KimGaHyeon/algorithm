import sys
sys.stdin = open("input/4881_input.txt", "r")
def find(row):
    global sum, result
    # 기존 결과가 더 작으면 그냥 return
    if result < sum:
        return
    # 마지막 row에 도달
    if row == n:
        # 기존 결과보다 작다면 result 갱신
        if result > sum:
            result = sum
        # 아니면 그냥 return
        return

    for col in range(n):
        # 방문하지 않은 col 에 대해 (유망한 경우)
        if not visited[col]:
            visited[col] = 1
            sum += board[row][col]
            # 다음 row 검사
            find(row+1)
            # 방문기록, sum 초기화  
            visited[col] = 0
            sum -= board[row][col]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    sum = 0
    result = 99999999
    find(0)
    print('#%d %d' % (test_case, result))