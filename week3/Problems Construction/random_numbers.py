from random import randint

def generate_random_list(n, start, end):
    random_list = []

    while n >= 1:
        random_list += [randint(start, end)]
        n -= 1

    return random_list
