# https://www.acmicpc.net/problem/5397
test_case = int(input())

for _ in range(test_case):
    data = list(input())
    cursor = -1
    pw = []
    for d in data:
        if d == '<':
            if cursor == 0:
                cursor = 0
            elif cursor >= 1:
                cursor -= 1
        elif d == '>':
            if cursor == len(pw)-1:
                continue
            cursor += 1
        elif d == '-':
            pw.pop(cursor)
        elif d.isalnum():
            cursor += 1
            pw.insert(cursor, d)

    print("".join(pw))

