import sys
sys.stdin = open("4839_input.txt", "r")
T = int(input())
def binary_search(page, target):
    left = 1
    right = page
    count = 0
    while left<=right:
        mid = int((left+right)/2)
        if mid==target:
            return count
        elif mid>target:
            right = mid
            count+=1
        elif mid<target:
            left = mid
            count+=1

for test_case in range(1, T + 1):
    P,A,B = map(int, input().split())
    countA = binary_search(P,A)
    countB = binary_search(P,B)
    if countA>countB:
        result = 'B'
    elif countA<countB:
        result = 'A'
    else:
        result = 0

    print("#{} {}".format(test_case, result))