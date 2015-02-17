n = input("n= ")
n = int(n)

counter = 1
sum_of_odds = 0

while counter <= n:
    if counter % 2 != 0:
        sum_of_odds = sum_of_odds + counter
        counter = counter + 1
    else:
        counter = counter + 1

print(sum_of_odds)
