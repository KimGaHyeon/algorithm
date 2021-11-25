from itertools import permutations

a = [1,2,3]
p = permutations(a, 2)
print(p) # <itertools.permutations object at 0x7f9b711ac9b0>

print(list(p)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

b = list(map(''.join, permutations(a,3)))
print(b)