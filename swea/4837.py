import sys
sys.stdin = open("4837_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    A = []
    lst = []

    for i in range(1, 13):
        A.append(i)

    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        lst.append(subset)

    len_lst = []
    for i in lst:
        if len(i)== n:
            len_lst.append(i)

    result = 0
    for i in len_lst:
        if sum(i) == k:
            result += 1

    print('#%s %d' %(test_case, result))