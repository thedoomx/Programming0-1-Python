def str_reverse(word):
    new_word = ""

    for ch in word:
        new_word = ch + new_word

    return new_word

def join(delimiter, items):
    new_string = ""

    index = 0

    while index < len(items):
        if index < len(items) - 1:
            new_string = new_string + str(items[index]) + str(delimiter)
        else:
            new_string = new_string + str(items[index])

        index += 1
    
    return new_string

def startswith(search, string):

    index = 0
    new_string = ""
    length = len(search)

    while length > 0:
        new_string += string[index]

        length -= 1
        index += 1

    if new_string == search:
        return True
    else:
        return False

def endswith(search, string):

    new_string = ""
    length = len(search)
    index = len(string) - 1

    while length > 0:
        new_string = string[index] + new_string

        index -= 1
        length -= 1

    if new_string == search:
        return True
    else:
        return False

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

    new_word = str_reverse(new_word)
    
    result = ""
    index = 0
    
    for ch in new_word:
        if ch == " ":
            index += 1
        else:
            break

    while index < len(new_word):
        result += new_word[index]

        index += 1

    return str_reverse(result)



































