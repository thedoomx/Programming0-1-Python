n = input("n = ")
n = int(n)

index = 1
min_n = 0

while index <= n:
    number = input("Input number: ")
    number = int(number)

    if number <= min_n:
        min_n = number

    index += 1

print("Min is: " + str(min_n))
