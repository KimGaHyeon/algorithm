import sys

sys.stdin = open('input/11545_input.txt', 'r')


def check(line):
    return 'X' if line.count('X') + line.count('T') == 4 else \
        'O' if line.count('O') + line.count('T') == 4 else \
            'Draw' if line.count('.') == 0 else 'Not Completed'


T = int(input())

for test_case in range(1, T + 1):
    game = []
    for i in range(4):
        row = list(input())
        game.append(row)
    if test_case != T:
        input()

    res = []

    # horizontal check
    for i in range(4):
        res.append(check(game[i]))
        # print(game[i])

    # vertical check
    for i in range(4):
        res.append(check([game[j][i] for j in range(4)]))
        # print([game[j][i] for j in range(4)])

    # cross check
    res.append(check([game[i][i] for i in range(4)]))
    # print([game[i][i] for i in range(4)])
    res.append(check([game[i][-i - 1] for i in range(4)]))
    # print([game[i][-i-1] for i in range(4)])

    result = 'X won' if 'X' in res else \
        'O won' if 'O' in res else \
            'Draw' if res.count('Draw') == 10 else 'Game has not completed'

    print('#{} {}'.format(test_case, result))

