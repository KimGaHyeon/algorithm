from itertools import combinations

def solution(orders, course):
    possible = [{} for _ in range(len(course))]
    for i in orders:
        for j in range(len(course)):
            for k in combinations(sorted(i), course[j]):
                print(k)
                temp = "".join(k)
                if temp in possible[j]:
                    possible[j][temp]+=1
                else:
                    possible[j].setdefault(temp, 1)

    answer = []

    for i in range(len(course)):
        if possible[i] == {}:
            continue
        max_num = max(possible[i].values())
        for j in possible[i]:
            if possible[i][j] == max_num and max_num != 1:
                answer.append(j)
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

solution(orders,course)