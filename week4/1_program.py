first_name = input("First name: ")
second_name = input("Second name: ")
last_name = input("Last name: ")
birth_year = input("Birth year: ")
birth_year = int(birth_year)
age = 2015 - birth_year

container = {
    "first_name": first_name,
    "second_name": second_name,
    "last_name": last_name,
    "birth_year": birth_year,
    "age": age
    }

print(container)


