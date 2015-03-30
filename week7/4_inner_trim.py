def inner_trim(string):
    result = string
    result = str_reverse(trim(str_reverse(trim(result))))
    list_of_whitespaces = []

    for index in range(0, len(result)):
        if result[index] == " ":
            if result[index + 1] == " ":
                list_of_whitespaces += [index + 1]

    final_result = ""

    for index in range(0, len(result)):
        if index not in list_of_whitespaces:
            final_result += result[index]

    return final_result

def str_reverse(word):
    new_word = ""

    for ch in word:
        new_word = ch + new_word

    return new_word

def trim(string):

    new_word = ""

    index = 0

    for ch in string:
        if ch == " ":
            index += 1
        else:
            break

    while index < len(string):
        new_word += string[index]

        index += 1

    return new_word
