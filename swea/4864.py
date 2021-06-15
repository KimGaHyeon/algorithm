import sys
sys.stdin = open("4864_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))