n = input("n= ")
n = int(n)

list_digits = []

while n != 0:
    digit = n % 10
    list_digits = [digit] + list_digits
    n = n // 10

print("List: " + str(list_digits))

new_n = 0

for i in list_digits:
    new_n = new_n * 10 + i

print("Number: " + str(new_n))
