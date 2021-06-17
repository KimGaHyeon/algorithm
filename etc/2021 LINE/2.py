input_str1 = "AaTa+!12-3" # [2]
input_str2 = "aaaaZZZZ)" # [2,3,4]
input_str3 = "CaCbCgCdC888834A" # [1,4,5]
input_str4 = "UUUUU" # [1,3,4,5]
input_str5 = "ZzZz9Z824" # [0]

from string import ascii_lowercase, ascii_uppercase

def solution(inp_str):
    answer = []
    if len(inp_str)<8 or len(inp_str)>15:
        answer.append(1)

    lowers = list(ascii_lowercase)
    uppers = list(ascii_uppercase)
    special = list("~!@#$%^&*")
    nums = []
    for i in range(10):
        nums.append(str(i))

    available = []
    available.append(lowers)
    available.append(uppers)
    available.append(special)
    available.append(str(nums))

    used = [0]*4
    removed = list(inp_str)
    for i in inp_str:
        for j in range(len(available)):
            if i in available[j]:
                removed.remove(i)
                used[j] = 1
    if removed:
        answer.append(2)

    if used.count(1)<3:
        answer.append(3)

    count = 0
    for i in range(0, len(inp_str)):
        if i==len(inp_str)-1:
            break
        if inp_str[i] == inp_str[i+1]:
            count += 1

    if count>=3:
        answer.append(4)

    for i in inp_str:
         if inp_str.count(i)>4:
            answer.append(5)
            break

    if not answer:
        answer.append(0)
    print(answer)
    return answer

solution(input_str1)
solution(input_str2)
solution(input_str3)
solution(input_str4)
solution(input_str5)
