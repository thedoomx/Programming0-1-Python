def string_matrix(matrix_width, strings):
    new_list = []
    
    for string in strings:
        if len(string) > matrix_width:
            new_string = ""
            index = 0

            while index < matrix_width:
                new_string += string[index]
                index += 1

            new_list += [new_string]
        else:
            new_string = ""

            new_string = string
            length = len(new_string)

            while length < matrix_width:
                new_string += "X"
                length += 1

            new_list += [new_string]

    print (add_new_lines(add_walls(new_list)))

def add_walls(new_list):
    result = new_list
    temp_list = []
    temp_string = ""
    

    for item in range(0, len(new_list)):
        temp_string = new_list[item]
        for index in range(0, len(temp_string)):
            temp_list += [temp_string[index]]
        for index2 in range(0, len(temp_list) - 1):
            temp_list[index2] += " | "
        temp_string_2 = ""
        for index3 in range(0, len(temp_list)):
            temp_string_2 += temp_list[index3]
        result[item] = temp_string_2
        
        temp_list = []
        temp_string = ""

    for index in range(0, len(result)):
        result[index] = "| " + result[index] + " |"
    
    return result

def add_new_lines(new_list):
    result = ""

    index = 0

    for item in new_list:
        if index < len(new_list) - 1:
            result += item + "\n"
        else:
            result += item

        index += 1

    return result

