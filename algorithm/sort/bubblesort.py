def bubblesort(data):
    for num in range(len(data)-1):
        swap = False
        for i in range(len(data)-num-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swap = True

        if swap == False:
            break;
    return data


print(bubblesort([3,2,1,4,9,5,8]))