scores = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]
def getScore(list):
    avg = sum(list)/len(list)
    if avg >= 90:
        return "A"
    elif 80 <= avg < 90:
        return "B"
    elif 70 <= avg < 80:
        return "C"
    elif 50 <= avg < 70:
        return "D"
    else:
        return "F"

def solution(scores):
    temp = []
    temp.extend(list(zip(*scores)))
    col= []
    for item in temp:
        col.append(list(item))
    print(col)
    grade = []
    for i in range(len(col)):
        if max(col[i]) <= col[i][i] and col[i].count(col[i][i]) == 1:
            del col[i][i]
        elif min(col[i]) >= col[i][i] and col[i].count(col[i][i]) == 1:
            del col[i][i]
        grade.append(getScore(col[i]))
    return ''.join(grade)

print(solution(scores))

