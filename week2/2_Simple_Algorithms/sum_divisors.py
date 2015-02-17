n = input("n= ")
n = int(n)

sum_divisors = 0
counter = 1

while counter < n:
    if n % counter == 0:
        sum_divisors += counter

    counter += 1

print("Divisors' sum is: " + str(sum_divisors))
