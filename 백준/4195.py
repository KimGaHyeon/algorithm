# https://www.acmicpc.net/problem/4195

test_case = int(input())
for _ in range(test_case):
    f = int(input())
    network = set()
    a,b = input().split()
    network.add(a)
    network.add(b)
    print(len(network))
    for _ in range(f-1):
        x, y = input().split()
        if x in network:
            network.add(y)
            print(len(network))
        elif y in network:
            network.add(x)
            print(len(network))
    # print(network)
