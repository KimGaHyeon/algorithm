import sys
sys.stdin = open("4836_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    red, blue = [], []
    purple = 0
    for i in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if color == 1:
                    red.append((x, y))
                elif color == 2:
                    blue.append((x, y))

    for i in range(len(red)):
        for j in range(len(blue)):
            if red[i][0] == blue[j][0] and red[i][1] == blue[j][1]:
                purple += 1



    print("#{} {}".format(test_case, purple))