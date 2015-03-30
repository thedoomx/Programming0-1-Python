n = input("Vuvedete nechetno chislo \"N\": ")
n = int(n)

if n % 2 == 0:
    print("Vuveli ste chetno chislo !")
else:
    array = []
    length = n
    while n >= 1:
        array += [n * "*"]

        n -= 2

    n += 4

    while n <= length:
        array += [n * "*"]

        n += 2

    max_length = len(array[0])

    for index in range(0, len(array)):
        if len(array[index]) != max_length:
            temp_length = (max_length - len(array[index])) / 2
            array[index] = "." * int(temp_length) + array[index] + "." * int(temp_length)




    result = ""

    for index in range(0, len(array) - 1):
        result += array[index] + "\n"

    result += array[len(array) - 1]

    print(result)
