n = input("n= ")
n = int(n)

index = 1
sum_numbers = 0

while index <= n:
    number = input("Input number: ")
    number = int(number)
    sum_numbers += number

    index += 1

print("The sum of all numbers is " + str(sum_numbers))
