n = input("n= ")
n = int(n)

divider = n
counter = 0

while divider > 0:
    if n % divider == 0:
        counter += 1
        divider -= 1
    else:
        divider -= 1

if counter > 2:
    print(str(n) + " is NOT prime.")
else:
    print(str(n) + " is prime.")

print(counter)
