n = input()
alpha = []
num = 0

for i in n:
    if i.isalpha():
        alpha.append(i)
    else:
        num += int(i)
alpha.sort()
alpha.append(str(num))

print(''.join(alpha))