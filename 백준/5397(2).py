# https://www.acmicpc.net/problem/5397

test_case = int(input())

for _ in range(test_case):
    left = []
    right = []
    data = input()
    for d in data:
        if d == "<":
            if left:
                right.append(left.pop())
        elif d == ">":
            if right:
                left.append(right.pop())
        elif d == "-":
            if left:
                left.pop()
        else:
            left.append(d)
    left.extend(reversed(right))
    print(''.join(left))