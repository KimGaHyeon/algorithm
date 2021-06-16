# https://programmers.co.kr/learn/courses/30/lessons/42888
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    dict = {}
    answer = []
    message = []
    for r in record:
        arr = r.split()
        if arr[0] == "Enter" or arr[0] == "Leave":
            temp = []
            temp.append(arr[0])
            temp.append(arr[1])
            message.append(temp)
        if arr[0] == "Enter" or arr[0] == "Change":
            dict[arr[1]] = arr[2]

    for m in message:
        str = ''
        if m[0] == "Enter":
            str += dict[m[1]] + "님이 들어왔습니다."
        elif m[0] == "Leave":
            str += dict[m[1]] + "님이 나갔습니다."
        answer.append(str)

    return answer


print(solution(record))