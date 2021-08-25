# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]>0:
                stack.append(board[i][m-1])
                board[i][m-1]=0
                if stack[-1:]==stack[-2:-1]:
                    answer+=2
                    stack = stack[:-2]
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)