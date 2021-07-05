enter = [1,4,2,3]
leave = [2,1,4,3]

room = []
meet = [0] * len(enter)

for l in leave:
    temp_enter = enter.copy()
    for e in temp_enter:
        if l in temp_enter:
            room.append(e)
            enter.pop(0)
        if l == e:
            break
    room.remove(l)
    meet[l - 1] += len(room)
    for r in room:
        meet[r - 1] += 1
print(meet)
