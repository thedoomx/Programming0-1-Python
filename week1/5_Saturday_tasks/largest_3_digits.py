n = input("Input 3 digit number: ")
a = n[0]
b = n[1]
c = n[2]

a = int(a)
b = int(b)
c = int(c)

largest_n = 0
middle_n = 0
lowest_n = 0

if a >= b and b >= c:
    largest_n = a
    middle_n = b
    lowest_n = c
elif a >= c and c >= b:
    largest_n = a
    middle_n = c
    lowest_n = b
elif b >= a and a >= c:
    largest_n = b
    middle_n = a
    lowest_n = c
elif b >= c and c >= a:
    largest_n = b
    middle_n = c
    lowest_n = a
elif c >= a and a >= b:
    largest_n = c
    middle_n = a
    lowest_n = b
elif c >= b and b >= a:
    largest_n = c
    middle_n = b
    lowest_n = a
else:
    print("Else ?Else what !?")

print(str(largest_n) + str(middle_n) + str(lowest_n))
print(str(lowest_n) + str(middle_n) + str(largest_n))
