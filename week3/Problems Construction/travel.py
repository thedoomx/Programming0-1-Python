def travel(travels):
    total_sum = 0
    for travel in travels:
        if travel >= 23:
            total_sum += 23
        else:
            total_sum += travel
        if total_sum >= 50:
            return 50

    return total_sum

print(travel([23, 24, 2]))
print(travel([28, 5, 23]))
print(travel([1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(travel([1] * 51))
