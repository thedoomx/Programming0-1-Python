n = input("n= ")
n = int(n)

sum_of_digits = 0

while n >= 1:
    sum_of_digits = sum_of_digits + (n % 10)
    n = n // 10

print(sum_of_digits)

