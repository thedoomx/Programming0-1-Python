n = input("n= ")
n = int(n)

counter = 1
sum_of_evens = 0

while counter <= n:
    if counter % 2 == 0:
        sum_of_evens = sum_of_evens + counter
        counter = counter + 1
    else:
        counter = counter + 1

print(sum_of_evens)
