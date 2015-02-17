a = input("a= ")
a = int(a)

b = input("b= ")
b = int(b)

while a <= b:
    if a % 2 == 0:
        print(str(a) + " - even")
        a = a + 1
    else:
        print(str(a) + " - odd")
        a = a + 1
