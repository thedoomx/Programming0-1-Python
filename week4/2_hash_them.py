def hash_them(keys, values):
    new_dict = {}

    start = 0
    while start < len(keys):
        if start >= len(values):
            value = None
            new_dict[keys[start]] = value
        else:
            new_dict[keys[start]] = values[start]

        start += 1

    return new_dict

print(hash_them(["key"], ["value"]))
print(hash_them(["key1", "key2"], ["value1"]))

