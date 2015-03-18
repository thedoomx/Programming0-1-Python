def last(n):
    return n[len(n) - 1]

def pre_last(n):
    return n[len(n) - 2]

def fib_list(n):
    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    result = [1, 1]
    
    while len(result) < n:
        next_fib = last(result) + pre_last(result)
        result += [next_fib]

    return result

def count_digits(n):
    count = 0

    while n != 0:
        count += 1
        n //= 10

    return count

def to_number(numbers):
    number = 0

    for i in numbers:
        multiplier = 10 ** count_digits(i)
        number = number * multiplier + i

    return number

def fib_number(n):
    return to_number(fib_list(n))

print(fib_number(10))
