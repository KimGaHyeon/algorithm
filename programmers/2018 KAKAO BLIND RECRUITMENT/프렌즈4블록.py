board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
m,n = 6,6
def solution(m, n, board):
    board = list(map(list, zip(*board)))

    def game(b):
        pops = 0
        temp = [i[:] for i in b]
        for i in range(1, n):
            for j in range(1, m):
                if b[i][j] == -1: continue
                if b[i][j] == b[i - 1][j] == b[i - 1][j - 1] == b[i][j - 1]:
                    temp[i][j], temp[i - 1][j], temp[i - 1][j - 1], temp[i][j - 1] = 0, 0, 0, 0

        for i, v in enumerate(temp):
            cnt = v.count(0)
            pops += cnt
            temp[i] = [-1] * cnt + [a for a in v if a != 0]
        return temp, pops

    answer = 0
    while True:
        board, pops = game(board)
        if pops == 0:  return answer
        answer += pops
print(solution(m,n,board))