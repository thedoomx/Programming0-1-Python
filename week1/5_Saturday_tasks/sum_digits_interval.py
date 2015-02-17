n = input("n= ")
n = int(n)

m = input("m= ")
m = int(m)

lower = 0
upper = 0

if n > m:
    lower = m
    upper = n
else:
    lower = n
    upper = m
    
while lower <= upper:
    
    temp = lower
    sum_temp = 0
    
    while temp >= 1:
        sum_temp = sum_temp + (temp % 10)
        temp = temp // 10
        
    print("Sum of digits of " + str(lower) + " = " + str(sum_temp))
    lower = lower + 1
    
