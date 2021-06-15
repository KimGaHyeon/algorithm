from string import ascii_lowercase
# new_id1 = "...!@BaT#*..y.abcdefghijklm"
new_id2 = "z-+.^."
# new_id3 = "=.="
# new_id4 = "123_.def"
# new_id5 = "abcdefghijklmn.p"

def solution(new_id):
    answer = ''
    # step1
    answer = new_id.lower()

    # step2
    available = list("-_.")
    lowers = list(ascii_lowercase)
    nums = []
    for i in range(10):
        nums.append(str(i))
    available.extend(lowers)
    available.extend(nums)
    remove_lst = []

    for i in answer:
        if i not in available:
            remove_lst.append(i)
    answer = [i for i in answer if i not in remove_lst]

    # step3 z-.. -> z-.
    if len(answer)>1:
        for i in range(len(answer)):
            print(i)
            if i==len(answer)-1:
                break
            if answer[i] == '.' and answer[i+1] == '.':
                del answer[i]
    # print(answer)

    # # step4
    # while answer:
    #     if answer[0]=='.':
    #         answer.pop(0)
    #     elif answer[-1]=='.':
    #         answer.pop(-1)
    #
    # # step5
    # if not answer:
    #     answer.append("a")
    #
    # # step6
    # if len(answer) >= 16:
    #     del answer[15:]
    #     if answer[-1] == '.':
    #         del answer[-1]
    #
    # # step7
    # if len(answer) <= 2:
    #     value = answer[-1]
    #     for i in range(3-len(answer)):
    #         answer.append(value)
    #
    #
    print("".join(answer))
    return answer

solution(new_id2)