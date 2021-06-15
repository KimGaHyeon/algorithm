import sys
sys.stdin = open("input/4873_input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    data = input()
    lst = []
    for d in data:
        # lst에 담긴 문자와 담으려고 하는 문자가 같으면 제거
        if lst and d == lst[-1]:
            lst.pop()
        else:
            lst.append(d)
    print('#{}'.format(tc), len(lst))