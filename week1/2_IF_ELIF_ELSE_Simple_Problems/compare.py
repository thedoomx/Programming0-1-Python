a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

if a > b:
    a = str(a)
    b = str(b)
    print("a(" + a + ") is bigger than b(" + b + ").")
elif a < b:
    a = str(a)
    b = str(b)
    print("b(" + b + ") is bigger that a(" + a + ").")
else:
    a = str(a)
    b = str(b)
    print("a(" + a + ") is equal to b(" + b + ").")
