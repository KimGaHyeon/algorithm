from itertools import combinations
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    data = []
    for i in range(1,col+1):
        data.extend(combinations(range(col),i))

    unique = []
    for d in data:
        temp = [tuple([item[i] for i in d]) for item in relation]
        if len(set(temp)) == row:
            unique.append(d)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])

    return len(answer)


print(solution(relation))