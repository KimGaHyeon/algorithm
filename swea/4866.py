import sys
sys.stdin = open("input/4866_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    data = input()
    N = len(data)
    stack = []
    for i in range(N):
        # 여는 괄호가 올 경우 stack에 저장
        if data[i] == "(" or data[i] == "{":
            stack.append(data[i])
        elif data[i] == ")" or data[i] == "}":
            # 닫는 괄호 이며 stack이 빈 경우 처음부터 닫는 괄호가 오는 경우
            if len(stack) == 0:
                stack = [data[i]]
                break
            # stack에 저장된 괄호와 일치하지 않는 경우
            elif (data[i] == "}" and stack[-1] != "{") or (data[i] == ")" and stack[-1] != "("):
                stack = [data[i]]
                break
            # stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
            else:
                stack.pop()

    if not len(stack):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')