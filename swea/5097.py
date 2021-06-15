import sys
sys.stdin = open("input/5097_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    index= m%n
    print("#{} {}".format(test_case, data[index]))