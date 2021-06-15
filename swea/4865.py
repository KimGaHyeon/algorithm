import sys
sys.stdin = open("input/4865_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = {}
    for i in str1:
        result[i] = str2.count(i)

    print(result)
    print("#{} {}".format(test_case, max(result.values())))