def solution(food_times, k):
    count = 0

    if sum(food_times) <= k:
        return -1

    while k:
        k -= 1
        for i in range(len(food_times)):
            if food_times[i] == 0:
                if i == len(food_times) - 1:
                    food_times[0] -= 1
                    count = 0
                else:
                    food_times[i + 1] -= 1
                    count = i + 1
            else:
                food_times[i] -= 1
                count = i;
    return count + 1

