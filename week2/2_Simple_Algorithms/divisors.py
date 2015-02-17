n = input("n= ")
n = int(n)

counter = 1
divisors = []

while counter < n:
    if n % counter == 0:
        divisors += [counter]

    counter += 1

print(divisors)
    
