import sys
sys.stdin = open("4843_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    result = []

    while data:
        max_index = data.index(max(data))
        result.append(data[max_index])
        data.pop(max_index)

        min_index = data.index(min(data))
        result.append(data[min_index])
        data.pop(min_index)

    print('#%s'%test_case, end=' ')
    for i in range(10):
        print(result[i], end=" ")
    print()