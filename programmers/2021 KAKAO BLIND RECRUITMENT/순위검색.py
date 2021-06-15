from itertools import combinations
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    data = {}
    for i in info:
        temp = i.split()
        cnd = temp[:-1]     # info의 점수 제외한 조건들
        score = int(temp[-1])

        for j in range(5):
            case = list(combinations(range(4),j))
            for c in case:
                new_cnd = cnd.copy()
                for t in c:
                    new_cnd[t] = '-'
                dash_cnd = '/'.join(new_cnd)
                if dash_cnd in data:
                    data[dash_cnd].append(score)
                else:
                    data[dash_cnd] = [score]

    for v in data.values():
        v.sort()

    for q in query:
        query_lst = [i for i in q.split() if i!= "and"]
        query_cnd = '/'.join(query_lst[:-1])    # query 점수 제외한 조건
        query_score = int(query_lst[-1])

        if query_cnd in data:   # data안에 찾는 쿼리값이 존재한다면
            target = data[query_cnd]
            if len(target)>0:     # binary search
                start, end = 0, len(target)
                while start != end and start != len(target):
                    if target[(start+end)//2] >= query_score:
                        end = (start+end)//2
                    else:
                        start = (start+end)//2 + 1
                answer.append(len(target)-start) # 해당 인덱스부터 끝까지
        else:
            answer.append(0)
    return answer

solution(info,query)