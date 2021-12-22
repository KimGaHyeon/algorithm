# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061
def possible(answer):
    for x, y, stuff in answer:
        # 기둥이면
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보이면
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 삭제
        if operate == 0:
            # 일단 삭제해보고
            answer.remove([x, y, stuff])
            # 안되면 다시 설치
            if not possible(answer):
                answer.append([x, y, stuff])
        # 설치
        if operate == 1:
            # 일단 설치해보고
            answer.append([x, y, stuff])
            # 안되면 다시 삭제
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)