def head(array):
    return array[0]

def last(array):
    return array[len(array) - 1]

def tail(array):
    new_array = []

    index = 1

    while index < len(array):
        new_array += [array[index]]

        index += 1

    return new_array

def equal_lists(array1, array2):
    equals = True

    index = 0

    if len(array1) == len(array2):
        while index < len(array1):
            if array1[index] != array2[index]:
                equals = False
                break

            index += 1

    else:
        equals = False

    return equals

def count_item(element, array):
    counter = 0

    for item in array:
        if element == item:
            counter += 1

    return counter

def take(n, array):
    new_array = []

    if n > len(array):
        n = len(array)
    
    index = 0

    while n > 0:
        new_array += [array[index]]

        n -= 1
        index += 1

    return new_array

def drop(n, array):
    new_array = []

    while n < len(array):
        new_array += [array[n]]

        n += 1
    
    return new_array
