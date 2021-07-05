# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    coords = {
        "*": [0, 0],
        0: [1, 0],
        "#": [2, 0],
        7: [0, 1],
        8: [1, 1],
        9: [2, 1],
        4: [0, 2],
        5: [1, 2],
        6: [2, 2],
        1: [0, 3],
        2: [1, 3],
        3: [2, 3],
    }

    left_at = coords["*"]
    right_at = coords["#"]

    for n in numbers:
        target = coords[n]
        if n in [1,4,7]:
            left_at = target
            answer+="L"
        elif n in [3,6,9]:
            right_at = target
            answer+="R"

        # 2,5,8,0일 경우
        else:
            left_d = sum([abs(a-b) for a,b in zip(left_at, target)])
            right_d = sum([abs(a-b) for a,b in zip(right_at, target)])

            # 왼손이 더 가까우면
            if left_d<right_d:
                left_at = target
                answer+="L"
            # 오른손이 더 가까우면
            elif left_d>right_d:
                right_at = target
                answer+="R"

            # 거리가 같으면
            else:
                if hand=="left":
                    answer += "L"
                    left_at = target
                elif hand=="right":
                    answer += "R"
                    right_at = target
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))

