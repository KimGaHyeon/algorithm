import sys
sys.stdin = open("input/4880_input.txt", "r")

def win(x, y):
    if (data[x-1] == 1 and data[y-1] == 3) or (data[x-1] == 1 and data[y-1] == 1):
        return x
    elif (data[x-1] == 2 and data[y-1] == 1) or (data[x-1] == 2 and data[y-1] == 2):
        return x
    elif (data[x-1] == 3 and data[y-1] == 2) or (data[x-1] == 3 and data[y-1] == 3):
        return x
    return y

def game(start, end):
    # 상대가 없을 때
    if start == end:
        return start
    group1 = game(start, (start+end)//2)
    group2 = game((start+end)//2+1, end)
    return win(group1, group2)

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    start = 1
    end = n
    print(f'#{test_case} {game(start, end)}')