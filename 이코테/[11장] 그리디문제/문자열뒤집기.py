data = input()
zero = 0
one = 0

if data[0]=='1':
    zero += 1
else:
    one += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            zero += 1
        else:
            one += 1

print(min(one,zero))
