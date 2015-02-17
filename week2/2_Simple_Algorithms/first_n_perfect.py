n = input("n= ")
n = int(n)
# n на брой перфектни числа

number_counter = 0
counter = 1
sum_divisors = 0
number = 1

while True:
    while counter < number:
        if number % counter == 0:
            sum_divisors += counter
        counter += 1
        
    if number == sum_divisors:
        print(number)
        number_counter += 1

    if number_counter == n:
        break

    number += 1
    sum_divisors = 0
    counter = 1
    

