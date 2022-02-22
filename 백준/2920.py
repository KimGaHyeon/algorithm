data = list(map(int,input().split()))
ascd_data = sorted(data)
desc_data = sorted(data, reverse=True)

if data == ascd_data:
    print("ascending")
elif data == desc_data:
    print("descending")
else:
    print("mixed")
