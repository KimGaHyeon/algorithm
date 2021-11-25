def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    OX = ["O" for _ in range(1, n + 1)]
    deleted = []
    k += 1

    for c in cmd:
        op = c[0]
        if op == "U":
            for _ in range(int(c[2])):
                k = linked_list[k][0]
        elif op == "D":
            for _ in range(int(c[2])):
                k = linked_list[k][1]
        elif op == "C":
            prev, next = linked_list[k]
            deleted.append([prev, next, k])
            OX[k - 1] = "X"

            if next == n + 1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n + 1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        elif op == "Z":
            prev, next, now = deleted.pop()
            OX[now - 1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n + 1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(OX)

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))