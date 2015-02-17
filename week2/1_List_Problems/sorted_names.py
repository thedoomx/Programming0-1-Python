n = input("n= ")
n = int(n)

index = 1
names = []

while index <= n:
    word = input("Enter a name: ")
    names = names + [word]

    index += 1

names = sorted(names)

print("Sorted names are: ")

for x in names:
    print(x)
