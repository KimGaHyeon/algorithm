input_str1 = "AaTa+!12-3" # [2]
input_str2 = "aaaaZZZZ)" # [2,3,4]
input_str3 = "CaCbCgCdC888834A" # [1,4,5]
input_str4 = "UUUUU" # [1,3,4,5]
input_str5 = "ZzZz9Z824" # [0]

def solution(inp_str):
    answer = []
    # step 1
    if len(inp_str)<8 or len(inp_str)>15:
        answer.append(1)

    # step 2
    corrected = ''
    for word in inp_str:
        if word.isalnum() or word in "~!@#$%^&*":
            corrected += word
    if not corrected == inp_str:
        answer.append(2)

    # step 3
    count = 0
    dict = {"lower":0, "upper":0, "special":0, "num":0}
    for word in corrected:
        if word.islower():
            dict["lower"] += 1
        elif word.isupper():
            dict["upper"] += 1
        elif word.isnumeric():
            dict["num"] += 1
        else:
            dict["special"] += 1
    for key in dict:
        if dict[key]==0: count+=1
    if count>=2:
        answer.append(3)

    # step 4
    count = 0
    for i in range(0, len(inp_str)):
        if i==len(inp_str)-1:
            break
        if inp_str[i] == inp_str[i+1]:
            count += 1

    if count>=3:
        answer.append(4)

    # step 5
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