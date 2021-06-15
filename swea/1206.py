import sys
sys.stdin = open("1206_input.txt", "r")
for test_case in range(10):
    n = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        nearby = max([building[i-2], building[i-1], building[i+1], building[i+2]])
        if building[i]>nearby:
            result += building[i]-nearby
    print("#{} {}".format(test_case+1, result))
