a = input("a= ")
a = int(a)

b = input("b= ")
b = int(b)

if a > b:
    while b <= a:
        print (b)
        b = b + 1
else:
    while a <= b:
        print (a)
        a = a + 1
