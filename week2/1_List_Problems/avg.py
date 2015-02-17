n = input("n= ")
n = int(n)

index = 1
avg = 0
sum_of_numbers = 0

while index <= n:
    number = input("Input number: ")
    number = int(number)
    sum_of_numbers += number
    
    index += 1

avg = sum_of_numbers / n

print("Avg is: " + str(avg))
