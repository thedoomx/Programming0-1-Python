def to_list(n):

    n_list = []
    
    while n != 0:
        digit = n % 10
        n_list += [digit]
        n //= 10

    return n_list

def to_int(n):

    number = 0

    for x in n:
        number = number * 10 + x

    return number

n = input("n= ")
n = int(n)

lowest = sorted(to_list(n))
highest = sorted(lowest, reverse=True)

lowest = to_int(lowest)
highest = to_int(highest)

print(lowest)
print(highest)
