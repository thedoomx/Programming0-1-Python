n = input("n= ")
n = int(n)

index = 1
max_number = 0

while index <= n:
    number = input("Input number: ")
    number = int(number)

    if number >= max_number:
        max_number = number

    index += 1

print("Max is: " + str(max_number))
