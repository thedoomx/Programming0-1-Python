def is_string_palindrom(string):
    temp = ""
    result = ""

    for ch in string:
        if ch not in ",.!?":
            temp += ch

    for ch in temp:
        if ch != " ":
            result += ch

    result = result.lower()
    reverse_result = ""

    for ch in result:
        reverse_result = ch + reverse_result

    if reverse_result == result:
        return True
    else:
        return False
