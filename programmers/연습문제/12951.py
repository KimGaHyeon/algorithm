def solution(s):
    s = s.split(' ')
    answer = []
    for word in s:
        if word[0].isalpha():
            word = word[0].upper() + word[1:].lower()
        answer.append(word)
    return ' '.join(answer)


s = "3people unFollowed me"
print(solution(s))

