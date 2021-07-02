input_str1 = "AaTa+!12-3" # [2]
input_str2 = "aaaaZZZZ)" # [2,3,4]
input_str3 = "CaCbCgCdC888834A" # [1,4,5]
input_str4 = "UUUUU" # [1,3,4,5]
input_str5 = "ZzZz9Z824" # [0]

def solution(inp_str):
    answer = set()
    # step 1
    if len(inp_str)<8 or len(inp_str)>15:
        answer.add(1)

    # step 2
    # 정규식 써서 고치기
    corrected = ''
    for word in inp_str:
        if word.isalnum() or word in "~!@#$%^&*":
            corrected += word
    if not corrected == inp_str:
        answer.add(2)

    # step 3
    x = set()
    for word in corrected:
        if word.islower():
            x.add("lower")
        elif word.isupper():
            x.add("upper")
        elif word.isnumeric():
            x.add("number")
        else:
            x.add("special")
    if len(x)<=2:
        answer.add(3)

    # step 4
    count = 0
    for i in range(0, len(inp_str)):
        if i==len(inp_str)-1:
            break
        if inp_str[i] == inp_str[i+1]:
            count += 1

    if count>=3:
        answer.add(4)

    # step 5
    for i in set(inp_str):
        if inp_str.count(i)>=5:
            answer.add(5)

    if not answer:
        answer.add(0)

    print(answer)
    return answer

solution(input_str1)
solution(input_str2)
solution(input_str3)
solution(input_str4)
solution(input_str5)