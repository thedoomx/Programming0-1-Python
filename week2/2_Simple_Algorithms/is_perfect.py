n = input("n= ")
n = int(n)

sum_divisors = 0
counter = 1

while counter < n:
    if n % counter == 0:
        sum_divisors += counter

    counter += 1

if sum_divisors == n:
    print(str(n) + " is a perfect number.")
else:
    print(str(n) + " is not a perfect number.")
