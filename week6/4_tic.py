def board_to_string(board):
    result = add_new_lines(add_walls(board))
    
    print(result)

def add_new_lines(board):
    result = ""

    index = 0
    for array in board:
        if index < len(board) - 1:
            for item in array:
                result += item
            result += "\n"
        else:
            for item in array:
                result += item

        index += 1

    print(result)

def add_walls(board):
    result = board

    for array in range(0, len(result)):
        for item in range(0, len(result[array]) - 1):
            result[array][item] += " | "

    for array in range(0, len(result)):
        result[array][0] = "| " + result[array][0]
        result[array][len(result) - 1] += " |"
    return result
