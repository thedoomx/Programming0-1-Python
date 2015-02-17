from random import randint

a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

operation = input("Enter operation: ")

if operation == "+" :
    print("Result is: \n" + str(a + b))
elif operation == "-" :
    print("Result is: \n" + str(a - b))
elif operation == "/" :
    print("Result is: \n" + str(a / b))
elif operation == "*" :
    print("Result is: \n" + str(a * b))
else:
    print("We do not support that operation.")
