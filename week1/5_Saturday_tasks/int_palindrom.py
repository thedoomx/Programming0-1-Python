n = input("n=  ")
n = int(n)

number = n
palindrom = ""

while number > 0:
    temp = number % 10
    palindrom = palindrom + str(temp)
    number //= 10

palindrom = int(palindrom)

if palindrom == n:
    print(str(n) + " is palindrom.")
else:
    print(str(n) + " is NOT palindrom.")



