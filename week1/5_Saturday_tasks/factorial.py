n = input("n= ")
n = int(n)

counter = n
n_factorial = 1

if n != 0:
    while counter > 1:
        n_factorial = n_factorial * counter
        counter = counter - 1
else:
    n_factorial = 1

print(str(n) + "! = " + str(n_factorial))

