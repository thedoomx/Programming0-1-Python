text = input("Text: ")

vowels = "aeiouyAEIOUY"
counter = 0

for i in text:
    if i in vowels:
        counter += 1

print("Vowels in text: " + str(counter))
