n = input("n= ")
n = int(n)

evens_counter = 0
evens = []
numbers = []

index = 1

while index <= n:
    number = input("Input number: ")
    number = int(number)
    numbers = numbers + [number]
    if number % 2 == 0:
        evens = evens + [number]
        evens_counter += 1

    index += 1

print("Count of evens: " + str(evens_counter))
print("Evens are: ")

for x in evens:
    print(x)

