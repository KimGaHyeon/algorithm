import sys
sys.stdin = open("input/4861_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = []
    data = []

    for _ in range(N):
        data.append(input())

    # 가로
    for r in range(N):
        for c in range(N - M + 1):
            if data[r][c: c + M] == data[r][c: c + M][:: -1]:
                result.append(data[r][c: c + M])

    # 세로
    for r in range(N - M + 1):
        for c in range(N):
            col_lst = []
            for i in range(M):  # 세로줄 입력
                col_lst.append(data[r + i][c])
            if col_lst == col_lst[:: -1]:  # 세로줄이 회문이면
                result.append(''.join(col_lst))

    print('#{} {}'.format(test_case, result[0]))
