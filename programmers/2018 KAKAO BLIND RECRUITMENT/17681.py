# https://programmers.co.kr/learn/courses/30/lessons/17681
n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]

def solution(n,arr1,arr2):
    arr1_bin = list(i[2:] for i in map(bin, arr1))
    arr2_bin = list(i[2:] for i in map(bin, arr2))
    answer = []
    for a,b in (zip(arr1_bin, arr2_bin)):
        answer.append(int(a)+int(b))

    answer = list(map(str, answer))
    answer = list(i.zfill(n) for i in answer)

    for i in range(n):
        answer[i] = answer[i].replace("1","#").replace("2","#").replace("0"," ")
    return answer

print(solution(n,arr1,arr2))
