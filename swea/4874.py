import sys
sys.stdin = open("input/4874_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    data = input().split()
    lst = []
    try:
        for i in data:
            if i == '.':
                result = lst.pop()
                if len(lst) != 0:
                    result = 'error'
                break
            elif i == '+':
                lst.append(lst.pop(-2) + lst.pop())
            elif i == '-':
                lst.append(lst.pop(-2) - lst.pop())
            elif i == '*':
                lst.append(lst.pop(-2) * lst.pop())
            elif i == '/':
                lst.append(lst.pop(-2) // lst.pop())
            else:
                lst.append(int(i))
    except:
        result = 'error'
    print('#{} {}'.format(test_case, result))