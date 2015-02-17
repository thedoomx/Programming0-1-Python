from random import randint

number = input("N = ")
number = int(number)

random_number = randint(1, number)
print(random_number)

random_number2 = randint(1, number)
print(random_number2)

random_number3 = randint(1, number)
print(random_number3)

print(random_number + random_number2 + random_number3)
