def reverse_int(number):
    new_int = 0
    digit_list = []
    
    while number != 0:
        digit = number % 10
        digit_list = digit_list + [digit]
        number //= 10

    for n in digit_list:
        new_int = n + new_int * 10

    return new_int

def sum_digits(n):
    sum_digits = 0

    while n != 0:
        digit = n % 10
        sum_digits += digit
        n //= 10

    return sum_digits

def product_digits(n):
    product = 1

    while n != 0:
        digit = n % 10
        product *= digit
        n //= 10

    return product


