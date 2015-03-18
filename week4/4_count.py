def count_vowels_constants(word):
    vowels = "aeiouyAEIOUY"
    constants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    new_dict = {
        "vowels": 0,
        "constants": 0
        }

    for i in word:
        if i in vowels:
            new_dict["vowels"] += 1
        else:
            new_dict["constants"] += 1

    return new_dict
    
