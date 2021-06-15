import sys
sys.stdin = open("input/11545_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    end = False
    n = 4 # 4*4 행렬
    lst = []
    row = []
    col = []
    l = [] # 왼쪽에서 시작하는 대각선 \
    r = [] # 오른쪽에서 시작하는 대각선 /

    for i in range(n):
        grid = list(input())
        lst.append(grid)

    if test_case != T:
        input()

    # 입력
    for i in range(n):
        for j in range(n):
            row.append(lst[i][j])
            col.append(lst[j][i])
        l.append(lst[i][i])
        r.append(lst[i][n-i-1])

    # 가로
    for i in range(0, len(row),4):
        if end:
            break
        if row[i:i+4].count("X")+row[i:i+4].count("T")==4:
            print("#%s X won"%test_case)
            end = True
        elif row[i:i+4].count("O")+row[i:i+4].count("T")==4:
            print("#%s O won"%test_case)
            end = True

    # 세로
    for i in range(0, len(col),4):
        if end:
            break
        if col[i:i+4].count("X")+col[i:i+4].count("T")==4:
            print("#%s X won"%test_case)
            end = True
        elif col[i:i+4].count("O")+col[i:i+4].count("T")==4:
            print("#%s O won"%test_case)
            end = True

    # \ 대각
    for i in range(0, len(l),4):
        if end:
            break
        if l[i:i+4].count("X")+l[i:i+4].count("T")==4:
            print("#%s X won"%test_case)
            end = True
        elif l[i:i+4].count("O")+l[i:i+4].count("T")==4:
            print("#%s O won"%test_case)
            end = True

    # / 대각
    for i in range(0, len(r),4):
        if end:
            break
        if r[i:i+4].count("X")+r[i:i+4].count("T")==4:
            print("#%s X won"%test_case)
            end = True
        elif r[i:i+4].count("O")+r[i:i+4].count("T")==4:
            print("#%s O won"%test_case)
            end = True

    # 비김
    draw_lst = []
    for i in range(len(lst)):
        for j in range(4):
            draw_lst.append(lst[i][j])

    if end==False:
        if '.' not in draw_lst:
            print("#%s Draw"%test_case)
            end = True
        # 안끝남
        else:
            print("#%s Game has not completed"%test_case)