word = input("Enter a word: ")

n = input("n= ")
n = int(n)

index = 1
array = []

while index <= n:
    word_1 = input("Enter a word: ")
    array = array + [word_1]

    index += 1

occurence_count = 0

for text in array:
    if word == text:
        occurence_count += 1

print(word + " is found " + str(occurence_count) + " times.")
