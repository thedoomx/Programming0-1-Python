def count_zero_neighbours(numbers):
    counter = 0

    index = 0

    while index < len(numbers):
        if numbers[index] + numbers[index + 1] == 0:
            counter += 1
            index += 2
        else:
            index += 1

    return counter

def count_zero_pairs(numbers):
    counter = 0
    
    index = 0

    while index < len(numbers):
        temp = numbers[index]
        inner_index = index
        
        while inner_index < len(numbers):
            if temp + numbers[inner_index] == 0:
                counter += 1
                
            inner_index += 1

        index += 1

    return counter

def is_prime(number):
    start = 2
    is_prime = True
    
    while start < number:
        if number % start == 0:
            is_prime = False
            break
        
        start += 1
        
    return is_prime

def prime_pair(numbers):
    has_pair = False
    
    for x in numbers:
        for y in numbers:
            if is_prime(x + y):
                has_pair = True
                break

    return has_pair
















    
