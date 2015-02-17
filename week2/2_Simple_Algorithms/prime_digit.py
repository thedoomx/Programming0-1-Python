n = input("n= ")
n = int(n)

digit = 0
counter = 1
prime_counter = 0
checker = False

while n != 0:
    digit = n % 10
    while counter <= digit:
        if digit % counter == 0:
            prime_counter += 1
        counter += 1

    if prime_counter == 2:
        checker = True
        break

    prime_counter = 0
    counter = 1
    n = n // 10

if checker == True:
    print("Yes")
else:
    print("No")
        
