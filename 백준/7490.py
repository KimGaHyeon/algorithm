# https://www.acmicpc.net/problem/7490
import copy

def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

tc = int(input())

for _ in range(tc):
    operators_list = []
    n = int(input())
    recursive([], n-1)

    integers = [i for i in range(1, n+1)]

    for operator in operators_list:
        result = ""
        for i in range(n-1):
            result += str(integers[i]) + operator[i]
        result += str(integers[-1])
        if eval(result.replace(' ', '')) == 0:
            print(result)
    print()
