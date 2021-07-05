ins = [3,2,1]
outs = [1,3,2]

in_at = [0]*len(ins)
out_at = [0]*len(outs)

for i in ins:
    in_at[i-1] = ins.index(i)+1
    out_at[i-1] = outs.index(i)+1

print("in_at:" , in_at)
print("out_at:" , out_at)

meet = [0]*len(ins)
for i in range(1, len(ins)+1):
    for j in range(1, len(ins)+1):
        # i+, j+, j-, i-
        if in_at[i-1]<in_at[j-1] and out_at[i-1]>out_at[j-1]:
            meet[i-1] += 1
            meet[j-1] += 1

print(meet)
