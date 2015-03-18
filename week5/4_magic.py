def magic_square(square):
    magic = True

    the_sum = sum_row(square[0])

    #proverqvame redove
    for numbers in square:
        if sum_row(numbers) != the_sum:
            magic = False
            break

    #proverqvame coloni        
    index_of_big = 0
    index_of_small = 0
    sum_of_col = 0
    
    while index_of_small < len(square):
        while index_of_big < len(square):
            sum_of_col += square[index_of_big][index_of_small]

            index_of_big += 1
            
        if sum_of_col != the_sum:
            magic = False
            break
        
        index_of_small += 1
        index_of_big = 0
        sum_of_col = 0

    #proverqvame glavniq diagonal
    if main_diagonal(square) != the_sum:
        magic = False

    #proverqvame vtorichniq diagonal
    if secondary_diagonal(square) != the_sum:
        magic = False
        
    return magic
        
def sum_row(numbers):
    result = 0

    for i in numbers:
        result += i

    return result


def main_diagonal(numbers):
    index = 0

    main_diagonal = 0

    while index < len(numbers):
        main_diagonal += numbers[index][index]

        index += 1

    return main_diagonal

def secondary_diagonal(numbers):
    index = len(numbers) - 1

    secondary_diagonal = 0

    while index >= 0:
        secondary_diagonal += numbers[index][index]

        index -= 1

    return secondary_diagonal



















