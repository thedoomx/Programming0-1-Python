n = input("Input a number: ")
n = int(n)

reverse_n = ""

while n > 0:
    temp = n % 10
    reverse_n = reverse_n + str(temp)
    n = n // 10

print(int(reverse_n))
