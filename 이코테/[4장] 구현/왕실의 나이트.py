current = input()
# a1
x = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
row = int(current[1])
col = x[current[0]]
count = 0
moves = [(2,1), (2,-1), (-2,1), (-2,-1), (-1,2), (-1,-2), (1,2), (1,-2)]

for move in moves:
    next_row = row + move[0]
    next_col = col + move[1]
    if next_row >= 1 and next_col >= 1 and next_row <= 8 and next_col <= 8:
        count += 1

print(count)
