n = input("n= ")
n = int(n)

numbers = []
highest_numbers = []
lowest_numbers = []

highest = 0
lowest = 0

while n != 0:
    number = n % 10
    numbers += [number]
    n = n // 10

numbers = sorted(numbers)
lowest_numbers = numbers

for x in numbers:
    highest_numbers = [x] + highest_numbers

multiplier = 1

for x in lowest_numbers:
    highest = highest + (x * multiplier)
    multiplier = multiplier * 10

multiplier = 1

for x in highest_numbers:
    lowest = lowest + (x * multiplier)
    multiplier = multiplier * 10

print("Highest number: " + str(highest))
print("Lowest number: " + str(lowest))
